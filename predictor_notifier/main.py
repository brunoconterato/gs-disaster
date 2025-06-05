import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database_session import get_db_connection, release_db_connection, SessionLocal
from predictor_notifier.fake_alert import create_fake_alert

def main():
    conn = get_db_connection()
    print("Successfully connected to the database!")
    
    # Create a database session
    db = SessionLocal()

    # TODO: remove this
    create_fake_alert(db)

    # TODO: load model
    # TODO: get data from db
    # TODO: predict

    # TODO: save prediction to db
    # TODO: save alert to db
    # TODO: send alert if prediction is greater than threshold
    
    # Close the session
    db.close()
    release_db_connection(conn)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        raise e
