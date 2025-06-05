from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager
from dotenv import load_dotenv
from datetime import datetime

# TODO: use the new sensor_measurement table

class SensorData():
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String)
    measure_time = Column(String)  # Time string from ESP32 (HH:MM)
    river_level_cm = Column(Float)
    temperature_c = Column(Float)
    air_humidity_pct = Column(Float)  # Renamed from soil_moisture
    rain_analog = Column(Float)      # Raw analog value
    received_at = Column(DateTime, default=datetime.now)