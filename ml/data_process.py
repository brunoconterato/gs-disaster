# data_process.py
# Functions for data processing in the ML pipeline.

import pandas as pd
import numpy as np
from datetime import datetime
from sqlalchemy.orm import Session
from db import crud
from db.database_session import SessionLocal
from typing import Optional
from dateutil.relativedelta import relativedelta


# --- Load and format data from the database instead of CSV ---
def get_segment_name_to_id(session: Session):
    """
    Returns a dict mapping segment_name (from DB) to id_segment.
    """
    segments = session.query(crud.models.RiverSegment).all()
    return {seg.segment_name: seg.id_segment for seg in segments}


def get_station_ids_by_segment(session: Session, segment_name_to_id=None):
    """
    Returns a dict mapping segment_name to a list of station_ids for all segments in the DB.
    """
    if segment_name_to_id is None:
        segment_name_to_id = get_segment_name_to_id(session)
    result = {}
    for seg_name, seg_id in segment_name_to_id.items():
        stations = (
            session.query(crud.models.MonitoringStation)
            .filter(crud.models.MonitoringStation.id_segment == seg_id)
            .all()
        )
        if stations:
            result[seg_name] = [st.id_station for st in stations]
    return result


def get_sensor_ids_by_type(session: Session, station_id: int):
    """
    Returns a dict mapping sensor type name (from DB) to a list of sensor_ids for a given station.
    No hardcoded types. Uses all types from the database.
    """
    sensor_types = session.query(crud.models.SensorType).all()
    result = {}
    for stype in sensor_types:
        sensors = (
            session.query(crud.models.Sensor)
            .filter(
                crud.models.Sensor.id_station == station_id,
                crud.models.Sensor.id_sensor_type == stype.id_sensor_type,
            )
            .all()
        )
        if sensors:
            result[stype.name] = [sensor.id_sensor for sensor in sensors]
    return result


def load_measurements(
    session: Session,
    sensor_id: int,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    """
    Loads all measurements for a given sensor_id as a DataFrame.
    Optionally filters by start_date and/or end_date (YYYY-MM-DD).
    """
    query = session.query(crud.models.SensorMeasurement).filter(
        crud.models.SensorMeasurement.id_sensor == sensor_id
    )
    if start_date:
        query = query.filter(crud.models.SensorMeasurement.timestamp >= start_date)
    if end_date:
        query = query.filter(crud.models.SensorMeasurement.timestamp <= end_date)
    measurements = query.all()
    records = []
    for m in measurements:
        records.append(
            {
                "datetime": m.timestamp,
                "value": (
                    float(m.measurement_value)
                    if m.measurement_value is not None
                    else None
                ),
            }
        )
    df = pd.DataFrame(records)
    df.set_index("datetime", inplace=True)
    return df


def load_data_from_db(start_date: Optional[str] = None, end_date: Optional[str] = None):
    session = SessionLocal()
    try:
        station_ids_by_segment = get_station_ids_by_segment(session)
        dfs = {}
        for segment_name, station_ids in station_ids_by_segment.items():
            for station_id in station_ids:
                sensor_types_dict = get_sensor_ids_by_type(session, station_id)
                for typ, sensor_id_list in sensor_types_dict.items():
                    if not sensor_id_list:
                        continue
                    for sensor_id in sensor_id_list:
                        df = load_measurements(session, sensor_id, start_date, end_date)
                        col_name = f"{typ}_{segment_name}__station_{station_id}_sensor_{sensor_id}"
                        dfs[col_name] = df.rename(columns={"value": col_name})
        from functools import reduce

        all_dfs = list(dfs.values())
        if all_dfs:
            data = reduce(lambda left, right: left.join(right, how="outer"), all_dfs)
            data.sort_index(inplace=True)
        else:
            data = pd.DataFrame()
        return data
    finally:
        session.close()


def format_db_data_columns(data):
    """
    Reformat columns from DB-loaded DataFrame to match expected names:
    rain_upstream, level_upstream, flow_upstream, ...
    Uses station_1 as upstream, station_2 as downstream, station_3 as after.
    """
    mapping = {
        "rain_Região Metropolitana de Goiânia__station_1": "rain_upstream",
        "level_Região Metropolitana de Goiânia__station_1": "level_upstream",
        "flow_Região Metropolitana de Goiânia__station_1": "flow_upstream",
        "rain_Região Metropolitana de Goiânia__station_2": "rain_downstream",
        "level_Região Metropolitana de Goiânia__station_2": "level_downstream",
        "flow_Região Metropolitana de Goiânia__station_2": "flow_downstream",
        "rain_Região Metropolitana de Goiânia__station_3": "rain_after",
        "level_Região Metropolitana de Goiânia__station_3": "level_after",
        "flow_Região Metropolitana de Goiânia__station_3": "flow_after",
    }
    new_cols = {}
    for col in data.columns:
        for prefix, target in mapping.items():
            if col.startswith(prefix):
                new_cols[col] = target
    data = data[list(new_cols.keys())]
    data = data.rename(columns=new_cols)
    return data


def print_missing_values(data):
    missing_values = data.isnull().sum()
    print("Missing values in each column:")
    print(missing_values[missing_values > 0])


def fill(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the dataset.
    For rain columns, set missing values to 0.
    For flow and level columns, use backward fill (bfill).
    """
    rain_cols = [col for col in df.columns if "rain" in col]
    df[rain_cols] = df[rain_cols].fillna(0)
    flow_level_cols = [col for col in df.columns if ("flow" in col or "level" in col)]
    # Backward fill for flow and level columns, then ensure values are > 0 and not null
    df[flow_level_cols] = df[flow_level_cols].bfill()
    for col in flow_level_cols:
        df[col] = df[col].where(df[col] > 0, np.nan)
    df[flow_level_cols] = df[flow_level_cols].bfill()
    return df


def get_day_of_year_index(date: datetime):
    """Convert date to day of year."""
    return datetime(date.year, date.month, date.day).timetuple().tm_yday - 1


def get_sin_cos(x: float):
    """Convert x to sin and cos."""
    rad = 2 * np.pi * x
    return (np.sin(rad), np.cos(rad))


def encode_date(date: datetime):
    is_leap_year = 1 if date.year % 4 == 0 else 0
    total_year_days = 366 if is_leap_year else 365
    day_index = get_day_of_year_index(date)
    return get_sin_cos(day_index / total_year_days)


def resample_data(data: pd.DataFrame, fill_func=None) -> pd.DataFrame:
    """
    Resample the data to daily frequency and aggregate with mean, max, min, q25, q75.
    Optionally applies a fill function after resampling.
    """
    agg_ops = [
        ("mean", "mean"),
        ("max", "max"),
        ("min", "min"),
        ("q25", lambda x: x.quantile(0.25)),
        ("q75", lambda x: x.quantile(0.75)),
    ]
    agg_dict = {}
    for col in data.columns:
        for name, func in agg_ops:
            agg_dict[f"{col}_{name}"] = pd.NamedAgg(column=col, aggfunc=func)
    data_resampled = data.resample("D").agg(**agg_dict)
    data_resampled.reset_index(inplace=True)
    data_resampled.rename(columns={"datetime": "date"}, inplace=True)
    data_resampled.set_index("date", inplace=True)
    if fill_func is not None:
        data_resampled = fill_func(data_resampled)
    return data_resampled


def feature_engineering(data_resampled, encode_date_func=None):
    """
    Adds feature engineering columns to the resampled dataframe.
    - Accumulated rain for 2 and 3 days
    - Sine and cosine encoding for date
    - Year column
    """
    df = data_resampled.copy()
    df["rain_upstream_acc_2_days"] = df["rain_upstream_mean"].rolling(window=2).sum()
    df["rain_downstream_acc_2_days"] = (
        df["rain_downstream_mean"].rolling(window=2).sum()
    )
    df["rain_after_acc_2_days"] = df["rain_after_mean"].rolling(window=2).sum()
    df["rain_upstream_acc_3_days"] = df["rain_upstream_mean"].rolling(window=3).sum()
    df["rain_downstream_acc_3_days"] = (
        df["rain_downstream_mean"].rolling(window=3).sum()
    )
    df["rain_after_acc_3_days"] = df["rain_after_mean"].rolling(window=3).sum()
    if encode_date_func is not None:
        df[["date_sin", "date_cos"]] = df.index.to_series().apply(
            lambda x: pd.Series(encode_date_func(x.to_pydatetime()))
        )
    else:
        df[["date_sin", "date_cos"]] = df.index.to_series().apply(
            lambda x: pd.Series((np.nan, np.nan))
        )
    df["year"] = df.index.to_series().apply(lambda x: x.year)
    return df


def adjust_date_range(start_date: Optional[str], end_date: Optional[str]) -> tuple:
    """
    Adjusts the date range by extending it by one month backward for the start date
    and one month forward for the end date.
    """
    db_start_date = start_date
    db_end_date = end_date
    if start_date:
        dt = datetime.strptime(start_date, "%Y-%m-%d")
        db_start_date = (dt - relativedelta(months=1)).strftime("%Y-%m-%d")
    if end_date:
        dt = datetime.strptime(end_date, "%Y-%m-%d")
        db_end_date = (dt + relativedelta(months=1)).strftime("%Y-%m-%d")
    return db_start_date, db_end_date


def load_and_process_data_from_db(
    save_path=None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> pd.DataFrame:
    """
    Complete pipeline: load, clean, resample, feature engineer, and optionally save processed data.
    Returns the processed DataFrame.
    Accepts optional start_date and end_date (YYYY-MM-DD) to filter data loaded from DB.
    """
    # Adjust date range for DB loading
    db_start_date, db_end_date = adjust_date_range(start_date, end_date)

    # Load and format
    data = load_data_from_db(start_date=db_start_date, end_date=db_end_date)
    data = format_db_data_columns(data)

    # Fill missing values
    data = fill(data)

    # Resample
    data_resampled = resample_data(data, fill_func=fill)

    # Feature engineering
    data_resampled = feature_engineering(data_resampled, encode_date_func=encode_date)

    # Ensure index is DatetimeIndex for filtering
    if not isinstance(data_resampled.index, pd.DatetimeIndex):
        data_resampled.index = pd.to_datetime(data_resampled.index)

    # Filter years
    mask = (data_resampled.index.year <= 2024) & (data_resampled.index.year >= 2014)
    data_filtered = data_resampled[mask]

    # Final filter to requested range
    if start_date:
        data_filtered = data_filtered[data_filtered.index >= start_date]
    if end_date:
        data_filtered = data_filtered[data_filtered.index <= end_date]

    # Save if requested
    if save_path is not None:
        data_filtered.to_csv(save_path, sep=";", index=True)
        print(f"Processed data saved to {save_path}")

    return data_filtered
