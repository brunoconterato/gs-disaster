from sqlalchemy.orm import Session
from sqlalchemy import Table, select
from database_session import Base
from db import models


# ------------------- River -------------------
def create_river(db: Session, river_name: str, description: str = None):
    river = models.River(river_name=river_name, description=description)
    db.add(river)
    db.commit()
    db.refresh(river)
    return river


def get_river(db: Session, river_id: int):
    return db.query(models.River).filter(models.River.id_river == river_id).first()


def get_rivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.River).offset(skip).limit(limit).all()


def update_river(
    db: Session, river_id: int, river_name: str = None, description: str = None
):
    river = get_river(db, river_id)
    if river_name is not None:
        river.river_name = river_name
    if description is not None:
        river.description = description
    db.commit()
    db.refresh(river)
    return river


def delete_river(db: Session, river_id: int):
    river = get_river(db, river_id)
    db.delete(river)
    db.commit()
    return river


# ------------------- RiverSegment -------------------
def create_river_segment(
    db: Session,
    id_river: int,
    segment_name: str,
    location_description: str = None,
    geographic_coordinates=None,
    critical_threshold_level=None,
):
    segment = models.RiverSegment(
        id_river=id_river,
        segment_name=segment_name,
        location_description=location_description,
        geographic_coordinates=geographic_coordinates,
        critical_threshold_level=critical_threshold_level,
    )
    db.add(segment)
    db.commit()
    db.refresh(segment)
    return segment


def get_river_segment(db: Session, segment_id: int):
    return (
        db.query(models.RiverSegment)
        .filter(models.RiverSegment.id_segment == segment_id)
        .first()
    )


def get_river_segments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RiverSegment).offset(skip).limit(limit).all()


def update_river_segment(db: Session, segment_id: int, **kwargs):
    segment = get_river_segment(db, segment_id)
    for key, value in kwargs.items():
        setattr(segment, key, value)
    db.commit()
    db.refresh(segment)
    return segment


def delete_river_segment(db: Session, segment_id: int):
    segment = get_river_segment(db, segment_id)
    db.delete(segment)
    db.commit()
    return segment


# ------------------- StationType -------------------
def create_station_type(db: Session, name: str, description: str = None):
    station_type = models.StationType(name=name, description=description)
    db.add(station_type)
    db.commit()
    db.refresh(station_type)
    return station_type


def get_station_type(db: Session, station_type_id: int):
    return (
        db.query(models.StationType)
        .filter(models.StationType.id_station_type == station_type_id)
        .first()
    )


def get_station_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StationType).offset(skip).limit(limit).all()


def update_station_type(
    db: Session, station_type_id: int, name: str = None, description: str = None
):
    station_type = get_station_type(db, station_type_id)
    if name is not None:
        station_type.name = name
    if description is not None:
        station_type.description = description
    db.commit()
    db.refresh(station_type)
    return station_type


def delete_station_type(db: Session, station_type_id: int):
    station_type = get_station_type(db, station_type_id)
    db.delete(station_type)
    db.commit()
    return station_type


# ------------------- MonitoringStation -------------------
def create_monitoring_station(
    db: Session,
    id_segment: int,
    id_station_type: int,
    station_name: str,
    geographic_location=None,
    installation_date=None,
    status="Active",
):
    station = models.MonitoringStation(
        id_segment=id_segment,
        id_station_type=id_station_type,
        station_name=station_name,
        geographic_location=geographic_location,
        installation_date=installation_date,
        status=status,
    )
    db.add(station)
    db.commit()
    db.refresh(station)
    return station


def get_monitoring_station(db: Session, station_id: int):
    return (
        db.query(models.MonitoringStation)
        .filter(models.MonitoringStation.id_station == station_id)
        .first()
    )


def get_monitoring_stations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MonitoringStation).offset(skip).limit(limit).all()


def update_monitoring_station(db: Session, station_id: int, **kwargs):
    station = get_monitoring_station(db, station_id)
    for key, value in kwargs.items():
        setattr(station, key, value)
    db.commit()
    db.refresh(station)
    return station


def delete_monitoring_station(db: Session, station_id: int):
    station = get_monitoring_station(db, station_id)
    db.delete(station)
    db.commit()
    return station


# ------------------- SensorType -------------------
def create_sensor_type(
    db: Session, name: str, unit_of_measure: str, description: str = None
):
    sensor_type = models.SensorType(
        name=name, unit_of_measure=unit_of_measure, description=description
    )
    db.add(sensor_type)
    db.commit()
    db.refresh(sensor_type)
    return sensor_type


def get_sensor_type(db: Session, sensor_type_id: int):
    return (
        db.query(models.SensorType)
        .filter(models.SensorType.id_sensor_type == sensor_type_id)
        .first()
    )


def get_sensor_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SensorType).offset(skip).limit(limit).all()


def update_sensor_type(db: Session, sensor_type_id: int, **kwargs):
    sensor_type = get_sensor_type(db, sensor_type_id)
    for key, value in kwargs.items():
        setattr(sensor_type, key, value)
    db.commit()
    db.refresh(sensor_type)
    return sensor_type


def delete_sensor_type(db: Session, sensor_type_id: int):
    sensor_type = get_sensor_type(db, sensor_type_id)
    db.delete(sensor_type)
    db.commit()
    return sensor_type


# ------------------- Sensor -------------------
def create_sensor(
    db: Session,
    id_station: int,
    id_sensor_type: int,
    sensor_identifier: str,
    model: str = None,
    calibration_date=None,
    status="Operational",
):
    sensor = models.Sensor(
        id_station=id_station,
        id_sensor_type=id_sensor_type,
        sensor_identifier=sensor_identifier,
        model=model,
        calibration_date=calibration_date,
        status=status,
    )
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.id_sensor == sensor_id).first()


def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).offset(skip).limit(limit).all()


def update_sensor(db: Session, sensor_id: int, **kwargs):
    sensor = get_sensor(db, sensor_id)
    for key, value in kwargs.items():
        setattr(sensor, key, value)
    db.commit()
    db.refresh(sensor)
    return sensor


def delete_sensor(db: Session, sensor_id: int):
    sensor = get_sensor(db, sensor_id)
    db.delete(sensor)
    db.commit()
    return sensor


# ------------------- SensorMeasurement -------------------
def create_sensor_measurement(
    db: Session,
    id_sensor: int,
    measurement_value,
    timestamp,
    data_source: str,
    quality_flag: str = None,
):
    measurement = models.SensorMeasurement(
        id_sensor=id_sensor,
        measurement_value=measurement_value,
        timestamp=timestamp,
        data_source=data_source,
        quality_flag=quality_flag,
    )
    db.add(measurement)
    db.commit()
    db.refresh(measurement)
    return measurement


def get_sensor_measurement(db: Session, measurement_id: int):
    return (
        db.query(models.SensorMeasurement)
        .filter(models.SensorMeasurement.id_measurement == measurement_id)
        .first()
    )


def get_sensor_measurements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SensorMeasurement).offset(skip).limit(limit).all()


def update_sensor_measurement(db: Session, measurement_id: int, **kwargs):
    measurement = get_sensor_measurement(db, measurement_id)
    for key, value in kwargs.items():
        setattr(measurement, key, value)
    db.commit()
    db.refresh(measurement)
    return measurement


def delete_sensor_measurement(db: Session, measurement_id: int):
    measurement = get_sensor_measurement(db, measurement_id)
    db.delete(measurement)
    db.commit()
    return measurement


# ------------------- MLModel -------------------
def create_ml_model(
    db: Session,
    model_name: str,
    model_type: str,
    training_date,
    performance_metrics=None,
    model_path: str = None,
    input_features_description=None,
    output_target_description=None,
    is_active=True,
):
    ml_model = models.MLModel(
        model_name=model_name,
        model_type=model_type,
        training_date=training_date,
        performance_metrics=performance_metrics,
        model_path=model_path,
        input_features_description=input_features_description,
        output_target_description=output_target_description,
        is_active=is_active,
    )
    db.add(ml_model)
    db.commit()
    db.refresh(ml_model)
    return ml_model


def get_ml_model(db: Session, model_id: int):
    return db.query(models.MLModel).filter(models.MLModel.id_model == model_id).first()


def get_ml_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MLModel).offset(skip).limit(limit).all()


def update_ml_model(db: Session, model_id: int, **kwargs):
    ml_model = get_ml_model(db, model_id)
    for key, value in kwargs.items():
        setattr(ml_model, key, value)
    db.commit()
    db.refresh(ml_model)
    return ml_model


def delete_ml_model(db: Session, model_id: int):
    ml_model = get_ml_model(db, model_id)
    db.delete(ml_model)
    db.commit()
    return ml_model


# ------------------- FloodPrediction -------------------
def create_flood_prediction(
    db: Session,
    id_model: int,
    id_station: int,
    prediction_timestamp,
    predicted_level=None,
    predicted_risk_level: str = None,
    forecast_horizon_minutes: int = None,
    prediction_confidence=None,
):
    prediction = models.FloodPrediction(
        id_model=id_model,
        id_station=id_station,
        prediction_timestamp=prediction_timestamp,
        predicted_level=predicted_level,
        predicted_risk_level=predicted_risk_level,
        forecast_horizon_minutes=forecast_horizon_minutes,
        prediction_confidence=prediction_confidence,
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_flood_prediction(db: Session, prediction_id: int):
    return (
        db.query(models.FloodPrediction)
        .filter(models.FloodPrediction.id_prediction == prediction_id)
        .first()
    )


def get_flood_predictions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FloodPrediction).offset(skip).limit(limit).all()


def update_flood_prediction(db: Session, prediction_id: int, **kwargs):
    prediction = get_flood_prediction(db, prediction_id)
    for key, value in kwargs.items():
        setattr(prediction, key, value)
    db.commit()
    db.refresh(prediction)
    return prediction


def delete_flood_prediction(db: Session, prediction_id: int):
    prediction = get_flood_prediction(db, prediction_id)
    db.delete(prediction)
    db.commit()
    return prediction


# ------------------- Alert -------------------
def create_alert(
    db: Session,
    id_prediction: int,
    alert_timestamp,
    alert_type: str,
    message: str,
    severity: str,
    status: str,
):
    alert = models.Alert(
        id_prediction=id_prediction,
        alert_timestamp=alert_timestamp,
        alert_type=alert_type,
        message=message,
        severity=severity,
        status=status,
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


def get_alert(db: Session, alert_id: int):
    return db.query(models.Alert).filter(models.Alert.id_alert == alert_id).first()


def get_alerts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Alert).offset(skip).limit(limit).all()


def update_alert(db: Session, alert_id: int, **kwargs):
    alert = get_alert(db, alert_id)
    for key, value in kwargs.items():
        setattr(alert, key, value)
    db.commit()
    db.refresh(alert)
    return alert


def delete_alert(db: Session, alert_id: int):
    alert = get_alert(db, alert_id)
    db.delete(alert)
    db.commit()
    return alert
