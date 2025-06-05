from db import crud
from datetime import datetime
from predictor_notifier.config import CONFIG

def create_fake_alert(db):
    # Create a fake flood prediction first (since alerts need a prediction)
    fake_prediction = crud.create_flood_prediction(
        db=db,
        id_model=CONFIG['model_id'],
        id_station=CONFIG['station_id'],
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
