from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Boolean,
    Text,
    ForeignKey,
    TIMESTAMP,
    Numeric,
    JSON,
)
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from db.database_session import Base


# River
class River(Base):
    __tablename__ = "river"
    id_river = Column(Integer, primary_key=True, autoincrement=True)
    river_name = Column(String, nullable=False)
    description = Column(Text)

    river_segments = relationship("RiverSegment", back_populates="river")

    def __repr__(self):
        return f"<River(id_river={self.id_river}, river_name='{self.river_name}')>"


# River Segment
class RiverSegment(Base):
    __tablename__ = "river_segment"
    id_segment = Column(Integer, primary_key=True, autoincrement=True)
    id_river = Column(Integer, ForeignKey("river.id_river"), nullable=False)
    segment_name = Column(String, nullable=False)
    location_description = Column(Text)
    geographic_coordinates = Column(Geometry("LINESTRING"))
    critical_threshold_level = Column(Numeric)

    river = relationship("River", back_populates="river_segments")
    monitoring_stations = relationship(
        "MonitoringStation", back_populates="river_segment"
    )

    def __repr__(self):
        return f"<RiverSegment(id_segment={self.id_segment}, segment_name='{self.segment_name}')>"


# Station Type
class StationType(Base):
    __tablename__ = "station_type"
    id_station_type = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    monitoring_stations = relationship(
        "MonitoringStation", back_populates="station_type"
    )

    def __repr__(self):
        return (
            f"<StationType(id_station_type={self.id_station_type}, name='{self.name}')>"
        )


# Monitoring Station
class MonitoringStation(Base):
    __tablename__ = "monitoring_station"
    id_station = Column(Integer, primary_key=True, autoincrement=True)
    id_segment = Column(Integer, ForeignKey("river_segment.id_segment"), nullable=False)
    id_station_type = Column(
        Integer, ForeignKey("station_type.id_station_type"), nullable=False
    )
    station_name = Column(String, nullable=False)
    geographic_location = Column(Geometry("POINT"))
    installation_date = Column(TIMESTAMP(timezone=True))
    status = Column(String, nullable=False, default="Active")

    river_segment = relationship("RiverSegment", back_populates="monitoring_stations")
    station_type = relationship("StationType", back_populates="monitoring_stations")
    sensors = relationship("Sensor", back_populates="monitoring_station")
    flood_predictions = relationship(
        "FloodPrediction", back_populates="monitoring_station"
    )

    def __repr__(self):
        return f"<MonitoringStation(id_station={self.id_station}, station_name='{self.station_name}')>"


# Sensor Type
class SensorType(Base):
    __tablename__ = "sensor_type"
    id_sensor_type = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_of_measure = Column(String, nullable=False)
    description = Column(Text)

    sensors = relationship("Sensor", back_populates="sensor_type")

    def __repr__(self):
        return f"<SensorType(id_sensor_type={self.id_sensor_type}, name='{self.name}')>"


# Sensor
class Sensor(Base):
    __tablename__ = "sensor"
    id_sensor = Column(Integer, primary_key=True, autoincrement=True)
    id_station = Column(
        Integer, ForeignKey("monitoring_station.id_station"), nullable=False
    )
    id_sensor_type = Column(
        Integer, ForeignKey("sensor_type.id_sensor_type"), nullable=False
    )
    sensor_identifier = Column(String, nullable=False)
    model = Column(String)
    calibration_date = Column(Date)
    status = Column(String, nullable=False, default="Operational")

    monitoring_station = relationship("MonitoringStation", back_populates="sensors")
    sensor_type = relationship("SensorType", back_populates="sensors")
    sensor_measurements = relationship("SensorMeasurement", back_populates="sensor")

    def __repr__(self):
        return f"<Sensor(id_sensor={self.id_sensor}, identifier='{self.sensor_identifier}')>"


# Sensor Measurement
class SensorMeasurement(Base):
    __tablename__ = "sensor_measurement"
    id_measurement = Column(Integer, primary_key=True, autoincrement=True)
    id_sensor = Column(Integer, ForeignKey("sensor.id_sensor"), nullable=False)
    measurement_value = Column(Numeric, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    data_source = Column(String, nullable=False)
    quality_flag = Column(String)

    sensor = relationship("Sensor", back_populates="sensor_measurements")

    def __repr__(self):
        return f"<SensorMeasurement(id_measurement={self.id_measurement}, timestamp={self.timestamp})>"


# ML Model Metric
class MLModelMetric(Base):
    __tablename__ = "ml_model_metric"
    id_metric = Column(Integer, primary_key=True, autoincrement=True)
    id_model = Column(Integer, ForeignKey("ml_model.id_model"), nullable=False)
    metric_name = Column(String, nullable=False)
    metric_value = Column(Numeric, nullable=False)
    description = Column(Text)

    ml_model = relationship("MLModel", back_populates="metrics")

    def __repr__(self):
        return f"<MLModelMetric(id_metric={self.id_metric}, name='{self.metric_name}', value={self.metric_value})>"


# ML Model
class MLModel(Base):
    __tablename__ = "ml_model"
    id_model = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, nullable=False)
    model_type = Column(String, nullable=False)
    training_date = Column(TIMESTAMP(timezone=True), nullable=False)
    performance_metrics = Column(JSON)
    model_path = Column(String)
    input_features_description = Column(JSON)
    output_target_description = Column(JSON)
    is_active = Column(Boolean, nullable=False, default=True)

    flood_predictions = relationship("FloodPrediction", back_populates="ml_model")
    metrics = relationship(
        "MLModelMetric", back_populates="ml_model", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<MLModel(id_model={self.id_model}, model_name='{self.model_name}')>"


# Flood Prediction
class FloodPrediction(Base):
    __tablename__ = "flood_prediction"
    id_prediction = Column(Integer, primary_key=True, autoincrement=True)
    id_model = Column(Integer, ForeignKey("ml_model.id_model"), nullable=False)
    id_station = Column(
        Integer, ForeignKey("monitoring_station.id_station"), nullable=False
    )
    prediction_timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    predicted_level = Column(Numeric)
    predicted_risk_level = Column(String)
    forecast_horizon_minutes = Column(Integer, nullable=False)
    prediction_confidence = Column(Numeric)

    ml_model = relationship("MLModel", back_populates="flood_predictions")
    monitoring_station = relationship(
        "MonitoringStation", back_populates="flood_predictions"
    )
    alerts = relationship("Alert", back_populates="flood_prediction")

    def __repr__(self):
        return f"<FloodPrediction(id_prediction={self.id_prediction}, timestamp={self.prediction_timestamp})>"


# Alert
class Alert(Base):
    __tablename__ = "alert"
    id_alert = Column(Integer, primary_key=True, autoincrement=True)
    id_prediction = Column(
        Integer, ForeignKey("flood_prediction.id_prediction"), nullable=False
    )
    alert_timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    alert_type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, nullable=False)

    flood_prediction = relationship("FloodPrediction", back_populates="alerts")

    def __repr__(self):
        return f"<Alert(id_alert={self.id_alert}, severity='{self.severity}')>"


class ResampledMeasurementsDaily(Base):
    __tablename__ = "resampled_measurements_daily"
    __table_args__ = {"extend_existing": True}

    date = Column(Date, primary_key=True)
    rain_upstream_mean = Column(Float)
    rain_upstream_max = Column(Float)
    rain_upstream_min = Column(Float)
    rain_upstream_q25 = Column(Float)
    rain_upstream_q75 = Column(Float)
    level_upstream_mean = Column(Float)
    level_upstream_max = Column(Float)
    level_upstream_min = Column(Float)
    level_upstream_q25 = Column(Float)
    level_upstream_q75 = Column(Float)
    flow_upstream_mean = Column(Float)
    flow_upstream_max = Column(Float)
    flow_upstream_min = Column(Float)
    flow_upstream_q25 = Column(Float)
    flow_upstream_q75 = Column(Float)
    rain_downstream_mean = Column(Float)
    rain_downstream_max = Column(Float)
    rain_downstream_min = Column(Float)
    rain_downstream_q25 = Column(Float)
    rain_downstream_q75 = Column(Float)
    level_downstream_mean = Column(Float)
    level_downstream_max = Column(Float)
    level_downstream_min = Column(Float)
    level_downstream_q25 = Column(Float)
    level_downstream_q75 = Column(Float)
    flow_downstream_mean = Column(Float)
    flow_downstream_max = Column(Float)
    flow_downstream_min = Column(Float)
    flow_downstream_q25 = Column(Float)
    flow_downstream_q75 = Column(Float)
    rain_after_mean = Column(Float)
    rain_after_max = Column(Float)
    rain_after_min = Column(Float)
    rain_after_q25 = Column(Float)
    rain_after_q75 = Column(Float)
    level_after_mean = Column(Float)
    level_after_max = Column(Float)
    level_after_min = Column(Float)
    level_after_q25 = Column(Float)
    level_after_q75 = Column(Float)
    flow_after_mean = Column(Float)
    flow_after_max = Column(Float)
    flow_after_min = Column(Float)
    flow_after_q25 = Column(Float)
    flow_after_q75 = Column(Float)
