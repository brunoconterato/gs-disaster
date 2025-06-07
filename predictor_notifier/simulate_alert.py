import sys
import os
from datetime import datetime

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database_session import get_db_connection, release_db_connection, SessionLocal
from predictor_notifier.fake_alert import create_fake_alert
from predictor_notifier.notifier import notify_alert, check_alert_webhook_credentials

def main():
    check_alert_webhook_credentials()

    conn = get_db_connection()
    print("Successfully connected to the database!")

    # Cria sessão com o banco
    db = SessionLocal()

    print("[INFO] Creating a fake alert...")
    create_fake_alert(db)

    print("[INFO] Notifying the fake alert...")
    notify_alert(
        alert_id="1",
        alert_timestamp=datetime.now(),
        alert_type="Flood Warning",
        message="High risk of flooding detected in the next day",
        severity="High",
        status="Active"
    )
    
    print("[INFO] Alert sent successfully!")

    db.close()
    release_db_connection(conn)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        raise e
