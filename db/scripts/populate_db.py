import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crud import *
from database_session import get_db, engine

from datetime import datetime
import pandas as pd
from tqdm import tqdm
from sqlalchemy import text
import io

# 1. River
river_data = {
    "river_name": "Rio Meia Ponte",
    "description": "Rio que atravessa Goiânia / GO",
}

# 2. RiverSegment
segment_data = {
    "segment_name": "Região Metropolitana de Goiânia",
    "location_description": "Trecho do Rio Meia Ponte que atravessa a Região Metropolitana de Goiânia, abrangendo áreas urbanas e rurais próximas à capital.",
    "geographic_coordinates": None,
    "critical_threshold_level": None,
}

# 3. StationType
station_type_data = {
    "name": "Fluviométrica",
    "description": "Estações destinadas à medição de variáveis hidrológicas, como nível e vazão dos rios.",
}

# 5. SensorTypes
sensor_types_data = [
    {
        "name": "rain",
        "unit_of_measure": "mm",
        "description": "Sensor para medir a quantidade de precipitação (chuva) em milímetros.",
    },
    {
        "name": "flow",
        "unit_of_measure": "m³/s",
        "description": "Sensor para medir a vazão do rio em metros cúbicos por segundo.",
    },
    {
        "name": "level",
        "unit_of_measure": "m",
        "description": "Sensor para medir o nível da água do rio em metros.",
    },
]

# 4. MonitoringStations
stations_data = [
    {
        "station_name": "MONTANTE DE GOIÂNIA",
        "geographic_location": "POINT(-49.2648 -16.6869)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona urbana inicial - Goiânia",
    },
    {
        "station_name": "JUSANTE DE GOIÂNIA",
        "geographic_location": "POINT(-49.2095 -16.7533)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona urbana densa - Goiânia",
    },
    {
        "station_name": "UHE SÃO SIMÃO FAZENDA BONITA DE BAIXO",
        "geographic_location": "POINT(-49.2267 -16.9658)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona rural - Hidrolândia - alguns kms após a cidade de Goiânia",
    },
]

# Station codes for sensor identifiers
station_codes = ["60640000", "60650000", "60655001"]
sensor_type_names = ["rain", "flow", "level"]

# Map raw columns to sensor IDs
RAW_SENSOR_COLUMN_TO_ID = {
    # Upstream
    ("upstream", "Chuva (mm)"): 1,
    ("upstream", "Vazão (m3/s)"): 2,
    ("upstream", "Nível (cm)"): 3,
    # Downstream
    ("downstream", "Chuva (mm)"): 4,
    ("downstream", "Vazão (m3/s)"): 5,
    ("downstream", "Nível (cm)"): 6,
    # After
    ("after", "Chuva (mm)"): 7,
    ("after", "Vazão (m3/s)"): 8,
    ("after", "Nível (cm)"): 9,
}


def save_raw_measurements(df, station, engine):
    # Prepare the data in the right format
    print("[INFO] Saving raw measurements to the database for ", station)
    rows = []
    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Saving {station} measurements", colour="cyan"):
        try:
            timestamp = pd.to_datetime(f"{row['Data']} {row['Hora']}", dayfirst=True)
        except Exception:
            continue
        for col in ["Chuva (mm)", "Vazão (m3/s)", "Nível (cm)"]:
            sensor_id = RAW_SENSOR_COLUMN_TO_ID.get((station, col))
            value = row.get(col)
            if sensor_id is not None and pd.notnull(value):
                rows.append([sensor_id, value, timestamp, "raw", ""])
    # Create a CSV in memory
    output = io.StringIO()
    for r in rows:
        output.write("\t".join([str(x) for x in r]) + "\n")
    output.seek(0)

    # Use psycopg2 to copy data
    conn = engine.raw_connection()  # FIX: use raw_connection for DBAPI
    cursor = conn.cursor()
    cursor.copy_from(
        output,
        "sensor_measurement",
        columns=(
            "id_sensor",
            "measurement_value",
            "timestamp",
            "data_source",
            "quality_flag",
        ),
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"[OK] Saved {station} raw measurements to the database.")


def load_and_save_raw_measurements(db):
    UPSTREAM_RAW_PATH = (
        "data/ANA HIDROWEB/RIO MEIA PONTE/60640000-MONTANTE DE GOIANIA.csv"
    )
    DOWNSTREAM_RAW_PATH = (
        "data/ANA HIDROWEB/RIO MEIA PONTE/60650000-JUSANTE DE GOIANIA.csv"
    )
    AFTER_RAW_PATH = "data/ANA HIDROWEB/RIO MEIA PONTE/60655001-UHE SAO SIMAO FAZENDA BONITA DE BAIXO.csv"

    upstream_data = pd.read_csv(
        UPSTREAM_RAW_PATH,
        sep=";",
        header=0,
        parse_dates=["Data"],
        dayfirst=False,
        low_memory=False,
    )
    upstream_data["Chuva (mm)"] = pd.to_numeric(
        upstream_data["Chuva (mm)"], errors="coerce"
    )
    upstream_data["Nível (cm)"] = pd.to_numeric(
        upstream_data["Nível (cm)"], errors="coerce"
    )
    upstream_data["Vazão (m3/s)"] = pd.to_numeric(
        upstream_data["Vazão (m3/s)"], errors="coerce"
    )
    upstream_data = upstream_data.loc[
        :, ~upstream_data.columns.str.contains("^Unnamed")
    ]

    downstream_data = pd.read_csv(
        DOWNSTREAM_RAW_PATH,
        sep=";",
        header=0,
        parse_dates=["Data"],
        dayfirst=False,
        low_memory=False,
    )
    downstream_data["Chuva (mm)"] = pd.to_numeric(
        downstream_data["Chuva (mm)"], errors="coerce"
    )
    downstream_data["Nível (cm)"] = pd.to_numeric(
        downstream_data["Nível (cm)"], errors="coerce"
    )
    downstream_data["Vazão (m3/s)"] = pd.to_numeric(
        downstream_data["Vazão (m3/s)"], errors="coerce"
    )
    downstream_data = downstream_data.loc[
        :, ~downstream_data.columns.str.contains("^Unnamed")
    ]

    after_data = pd.read_csv(
        AFTER_RAW_PATH,
        sep=";",
        header=0,
        parse_dates=["Data"],
        dayfirst=False,
        low_memory=False,
    )
    after_data["Chuva (mm)"] = pd.to_numeric(after_data["Chuva (mm)"], errors="coerce")
    after_data["Nível (cm)"] = pd.to_numeric(after_data["Nível (cm)"], errors="coerce")
    after_data["Vazão (m3/s)"] = pd.to_numeric(
        after_data["Vazão (m3/s)"], errors="coerce"
    )
    after_data = after_data.loc[:, ~after_data.columns.str.contains("^Unnamed")]

    save_raw_measurements(upstream_data, "upstream", engine)
    save_raw_measurements(downstream_data, "downstream", engine)
    save_raw_measurements(after_data, "after", engine)
    print("Saved all raw measurements to the database.")


def create_resampled_view(engine):
    with engine.connect() as conn:
        # Drop the view if it exists (CASCADE to drop dependent objects, e.g., model mapping)
        conn.execute(text("DROP VIEW IF EXISTS resampled_measurements_daily CASCADE;"))
        # Create the view with feature engineering columns
        conn.execute(
            text(
                """
                CREATE OR REPLACE VIEW resampled_measurements_daily AS
                WITH date_range AS (
                    SELECT generate_series(
                        (SELECT MIN(date_trunc('day', timestamp)) FROM sensor_measurement WHERE data_source = 'raw'),
                        (SELECT MAX(date_trunc('day', timestamp)) FROM sensor_measurement WHERE data_source = 'raw'),
                        interval '1 day'
                    )::date AS date
                ),
                base AS (
                    SELECT
                        date_trunc('day', timestamp) AS date,
                        id_sensor,
                        measurement_value
                    FROM sensor_measurement
                    WHERE data_source = 'raw'
                ),
                pivot AS (
                    SELECT
                        d.date,
                        -- Rain: fill missing with 0
                        COALESCE(AVG(CASE WHEN id_sensor = 1 THEN measurement_value END), 0) AS rain_upstream_mean,
                        COALESCE(MAX(CASE WHEN id_sensor = 1 THEN measurement_value END), 0) AS rain_upstream_max,
                        COALESCE(MIN(CASE WHEN id_sensor = 1 THEN measurement_value END), 0) AS rain_upstream_min,
                        COALESCE(percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 1 THEN measurement_value END), 0) AS rain_upstream_q25,
                        COALESCE(percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 1 THEN measurement_value END), 0) AS rain_upstream_q75,
                        AVG(CASE WHEN id_sensor = 3 THEN measurement_value END) AS level_upstream_mean,
                        MAX(CASE WHEN id_sensor = 3 THEN measurement_value END) AS level_upstream_max,
                        MIN(CASE WHEN id_sensor = 3 THEN measurement_value END) AS level_upstream_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 3 THEN measurement_value END) AS level_upstream_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 3 THEN measurement_value END) AS level_upstream_q75,
                        AVG(CASE WHEN id_sensor = 2 THEN measurement_value END) AS flow_upstream_mean,
                        MAX(CASE WHEN id_sensor = 2 THEN measurement_value END) AS flow_upstream_max,
                        MIN(CASE WHEN id_sensor = 2 THEN measurement_value END) AS flow_upstream_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 2 THEN measurement_value END) AS flow_upstream_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 2 THEN measurement_value END) AS flow_upstream_q75,
                        COALESCE(AVG(CASE WHEN id_sensor = 4 THEN measurement_value END), 0) AS rain_downstream_mean,
                        COALESCE(MAX(CASE WHEN id_sensor = 4 THEN measurement_value END), 0) AS rain_downstream_max,
                        COALESCE(MIN(CASE WHEN id_sensor = 4 THEN measurement_value END), 0) AS rain_downstream_min,
                        COALESCE(percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 4 THEN measurement_value END), 0) AS rain_downstream_q25,
                        COALESCE(percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 4 THEN measurement_value END), 0) AS rain_downstream_q75,
                        AVG(CASE WHEN id_sensor = 6 THEN measurement_value END) AS level_downstream_mean,
                        MAX(CASE WHEN id_sensor = 6 THEN measurement_value END) AS level_downstream_max,
                        MIN(CASE WHEN id_sensor = 6 THEN measurement_value END) AS level_downstream_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 6 THEN measurement_value END) AS level_downstream_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 6 THEN measurement_value END) AS level_downstream_q75,
                        AVG(CASE WHEN id_sensor = 5 THEN measurement_value END) AS flow_downstream_mean,
                        MAX(CASE WHEN id_sensor = 5 THEN measurement_value END) AS flow_downstream_max,
                        MIN(CASE WHEN id_sensor = 5 THEN measurement_value END) AS flow_downstream_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 5 THEN measurement_value END) AS flow_downstream_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 5 THEN measurement_value END) AS flow_downstream_q75,
                        COALESCE(AVG(CASE WHEN id_sensor = 7 THEN measurement_value END), 0) AS rain_after_mean,
                        COALESCE(MAX(CASE WHEN id_sensor = 7 THEN measurement_value END), 0) AS rain_after_max,
                        COALESCE(MIN(CASE WHEN id_sensor = 7 THEN measurement_value END), 0) AS rain_after_min,
                        COALESCE(percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 7 THEN measurement_value END), 0) AS rain_after_q25,
                        COALESCE(percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 7 THEN measurement_value END), 0) AS rain_after_q75,
                        AVG(CASE WHEN id_sensor = 9 THEN measurement_value END) AS level_after_mean,
                        MAX(CASE WHEN id_sensor = 9 THEN measurement_value END) AS level_after_max,
                        MIN(CASE WHEN id_sensor = 9 THEN measurement_value END) AS level_after_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 9 THEN measurement_value END) AS level_after_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 9 THEN measurement_value END) AS level_after_q75,
                        AVG(CASE WHEN id_sensor = 8 THEN measurement_value END) AS flow_after_mean,
                        MAX(CASE WHEN id_sensor = 8 THEN measurement_value END) AS flow_after_max,
                        MIN(CASE WHEN id_sensor = 8 THEN measurement_value END) AS flow_after_min,
                        percentile_cont(0.25) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 8 THEN measurement_value END) AS flow_after_q25,
                        percentile_cont(0.75) WITHIN GROUP (ORDER BY CASE WHEN id_sensor = 8 THEN measurement_value END) AS flow_after_q75
                    FROM date_range d
                    LEFT JOIN base b ON d.date = b.date
                    GROUP BY d.date
                ),
                filled AS (
                    SELECT
                        date,
                        rain_upstream_mean,
                        rain_upstream_max,
                        rain_upstream_min,
                        rain_upstream_q25,
                        rain_upstream_q75,
                        -- Level upstream: fill nulls with forward then backward fill
                        COALESCE(
                            LAST_VALUE(level_upstream_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_upstream_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_upstream_mean,
                        COALESCE(
                            LAST_VALUE(level_upstream_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_upstream_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_upstream_max,
                        COALESCE(
                            LAST_VALUE(level_upstream_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_upstream_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_upstream_min,
                        COALESCE(
                            LAST_VALUE(level_upstream_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_upstream_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_upstream_q25,
                        COALESCE(
                            LAST_VALUE(level_upstream_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_upstream_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_upstream_q75,
                        -- Flow upstream: fill nulls with forward then backward fill
                        COALESCE(
                            LAST_VALUE(flow_upstream_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_upstream_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_upstream_mean,
                        COALESCE(
                            LAST_VALUE(flow_upstream_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_upstream_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_upstream_max,
                        COALESCE(
                            LAST_VALUE(flow_upstream_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_upstream_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_upstream_min,
                        COALESCE(
                            LAST_VALUE(flow_upstream_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_upstream_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_upstream_q25,
                        COALESCE(
                            LAST_VALUE(flow_upstream_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_upstream_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_upstream_q75,
                        rain_downstream_mean,
                        rain_downstream_max,
                        rain_downstream_min,
                        rain_downstream_q25,
                        rain_downstream_q75,
                        COALESCE(
                            LAST_VALUE(level_downstream_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_downstream_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_downstream_mean,
                        COALESCE(
                            LAST_VALUE(level_downstream_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_downstream_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_downstream_max,
                        COALESCE(
                            LAST_VALUE(level_downstream_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_downstream_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_downstream_min,
                        COALESCE(
                            LAST_VALUE(level_downstream_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_downstream_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_downstream_q25,
                        COALESCE(
                            LAST_VALUE(level_downstream_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_downstream_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_downstream_q75,
                        COALESCE(
                            LAST_VALUE(flow_downstream_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_downstream_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_downstream_mean,
                        COALESCE(
                            LAST_VALUE(flow_downstream_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_downstream_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_downstream_max,
                        COALESCE(
                            LAST_VALUE(flow_downstream_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_downstream_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_downstream_min,
                        COALESCE(
                            LAST_VALUE(flow_downstream_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_downstream_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_downstream_q25,
                        COALESCE(
                            LAST_VALUE(flow_downstream_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_downstream_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_downstream_q75,
                        rain_after_mean,
                        rain_after_max,
                        rain_after_min,
                        rain_after_q25,
                        rain_after_q75,
                        COALESCE(
                            LAST_VALUE(level_after_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_after_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_after_mean,
                        COALESCE(
                            LAST_VALUE(level_after_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_after_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_after_max,
                        COALESCE(
                            LAST_VALUE(level_after_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_after_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_after_min,
                        COALESCE(
                            LAST_VALUE(level_after_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_after_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_after_q25,
                        COALESCE(
                            LAST_VALUE(level_after_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(level_after_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS level_after_q75,
                        COALESCE(
                            LAST_VALUE(flow_after_mean IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_after_mean IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_after_mean,
                        COALESCE(
                            LAST_VALUE(flow_after_max IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_after_max IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_after_max,
                        COALESCE(
                            LAST_VALUE(flow_after_min IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_after_min IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_after_min,
                        COALESCE(
                            LAST_VALUE(flow_after_q25 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_after_q25 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_after_q25,
                        COALESCE(
                            LAST_VALUE(flow_after_q75 IGNORE NULLS) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            FIRST_VALUE(flow_after_q75 IGNORE NULLS) OVER (ORDER BY date DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),
                            0
                        ) AS flow_after_q75
                    FROM pivot
                ),
                feat AS (
                    SELECT *,
                        -- Feature engineering: rolling sums (accumulated rain)
                        SUM(rain_upstream_mean) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rain_upstream_acc_2_days,
                        SUM(rain_downstream_mean) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rain_downstream_acc_2_days,
                        SUM(rain_after_mean) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rain_after_acc_2_days,
                        SUM(rain_upstream_mean) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rain_upstream_acc_3_days,
                        SUM(rain_downstream_mean) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rain_downstream_acc_3_days,
                        SUM(rain_after_mean) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rain_after_acc_3_days,
                        -- Date encodings
                        EXTRACT(YEAR FROM date) AS year,
                        SIN(2 * PI() * (EXTRACT(DOY FROM date)-1) / (CASE WHEN EXTRACT(YEAR FROM date) % 4 = 0 THEN 366 ELSE 365 END)) AS date_sin,
                        COS(2 * PI() * (EXTRACT(DOY FROM date)-1) / (CASE WHEN EXTRACT(YEAR FROM date) % 4 = 0 THEN 366 ELSE 365 END)) AS date_cos
                    FROM filled
                )
                SELECT * FROM feat
                ORDER BY date
                """
            )
        )
        conn.commit()


def main():
    print("[START] Populating database...")
    with get_db() as db:
        # River
        print("[INFO] Creating river...")
        river = create_river(db, **river_data)
        db.flush()
        river_id = getattr(river, "id_river", None)
        if not isinstance(river_id, int):
            river_id = river.__dict__["id_river"]
        print(f"[OK] River created with id: {river_id}")
        print("[INFO] Creating river segment...")
        segment = create_river_segment(
            db,
            id_river=river_id,
            segment_name=segment_data["segment_name"],
            location_description=segment_data["location_description"],
            geographic_coordinates=segment_data["geographic_coordinates"],
            critical_threshold_level=segment_data["critical_threshold_level"],
        )
        db.flush()
        segment_id = getattr(segment, "id_segment", None)
        if not isinstance(segment_id, int):
            segment_id = segment.__dict__["id_segment"]
        print(f"[OK] River segment created with id: {segment_id}")
        print("[INFO] Creating station type...")
        station_type = create_station_type(db, **station_type_data)
        db.flush()
        station_type_id = getattr(station_type, "id_station_type", None)
        if not isinstance(station_type_id, int):
            station_type_id = station_type.__dict__["id_station_type"]
        print(f"[OK] Station type created with id: {station_type_id}")
        # SensorTypes
        print("[INFO] Creating sensor types...")
        sensor_types = []
        for stype in tqdm(sensor_types_data, desc="Sensor Types", colour="green"):
            sensor_types.append(create_sensor_type(db, **stype))
        print(f"[OK] {len(sensor_types)} sensor types created.")
        # MonitoringStations
        print("[INFO] Creating monitoring stations...")
        stations = []
        for i, sdata in enumerate(tqdm(stations_data, desc="Stations", colour="blue")):
            station = create_monitoring_station(
                db,
                id_segment=segment_id,
                id_station_type=station_type_id,
                station_name=sdata["station_name"],
                geographic_location=sdata["geographic_location"],
                installation_date=sdata["installation_date"],
                status=sdata["status"],
            )
            stations.append(station)
        print(f"[OK] {len(stations)} monitoring stations created.")
        # Sensors
        print("[INFO] Creating sensors for each station...")
        total_sensors = 0
        for i, station in enumerate(
            tqdm(stations, desc="Stations for Sensors", colour="yellow")
        ):
            station_id = getattr(station, "id_station", None)
            if not isinstance(station_id, int):
                station_id = station.__dict__["id_station"]
            for j, sensor_type in enumerate(
                tqdm(
                    sensor_types,
                    desc=f"Sensors for Station {i+1}",
                    leave=False,
                    colour="magenta",
                )
            ):
                sensor_type_id = getattr(sensor_type, "id_sensor_type", None)
                if not isinstance(sensor_type_id, int):
                    sensor_type_id = sensor_type.__dict__["id_sensor_type"]
                sensor_identifier = f"{station_codes[i]}-{sensor_type.name}"
                create_sensor(
                    db,
                    id_station=station_id,
                    id_sensor_type=sensor_type_id,
                    sensor_identifier=sensor_identifier,
                    model="",  # Pass empty string instead of None
                    calibration_date=None,
                    status="Operational",
                )
                total_sensors += 1
        print(f"[OK] {total_sensors} sensors created.")
        # Save raw measurements after all sensors are created
        print("[INFO] Loading and saving raw measurements...")
        load_and_save_raw_measurements(db)
        print("[OK] Raw measurements loaded and saved.")

        # Create the resampled view after populating raw data
        print("[INFO] Creating resampled view...")
        create_resampled_view(engine)
        print("[OK] Resampled view created.")
        print("[SUCCESS] Database populated successfully.")


if __name__ == "__main__":
    main()
