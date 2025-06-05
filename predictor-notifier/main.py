import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db import crud, models

# Load environment variables
load_dotenv()

# Database connection configuration
DB_CONFIG = {
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'database': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD')
}

# Create SQLAlchemy engine and session
DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,  # minconn
    10, # maxconn
    **DB_CONFIG
)

def get_db_connection():
    return connection_pool.getconn()

def release_db_connection(conn):
    connection_pool.putconn(conn)

def create_fake_alert(db):
    fake_model_id = 1
    fake_station_id = 1
    
    # Create a fake flood prediction first (since alerts need a prediction)
    fake_prediction = crud.create_flood_prediction(
        db=db,
        id_model=fake_model_id,
        id_station=fake_station_id,
        prediction_timestamp=datetime.now(),
        predicted_level=2.5,
        predicted_risk_level="High",
        forecast_horizon_minutes=60,
        prediction_confidence=0.85
    )
    
    # Create a fake alert
    fake_alert = crud.create_alert(
        db=db,
        id_prediction=fake_prediction.id_prediction,
        alert_timestamp=datetime.now(),
        alert_type="Flood Warning",
        message="High risk of flooding detected in the next day",
        severity="High",
        status="Active"
    )
    
    print(f"Created alert with ID: {fake_alert.id_alert}")

# Test database connection and create a fake alert
try:
    conn = get_db_connection()
    print("Successfully connected to the database!")
    
    # Create a database session
    db = SessionLocal()

    create_fake_alert(db)
    
    # Close the session
    db.close()
    release_db_connection(conn)
except Exception as e:
    print(f"Error: {e}")

# TODO: load model
# TODO: get data from db
# TODO: predict

# TODO: save prediction to db
# TODO: save alert to db
# TODO: send alert if prediction is greater than threshold
