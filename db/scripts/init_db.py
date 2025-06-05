import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from db.database_session import get_db
from db.models import *
from db.database_session import Base
from sqlalchemy import text

# Database initialization
def init_db():
    with get_db() as db:
        with db.bind.connect() as conn:
            conn.execute(
                text("DROP VIEW IF EXISTS resampled_measurements_daily CASCADE;")
            )
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis;"))
            conn.commit()
        Base.metadata.drop_all(db.bind)  # Drop all tables
        Base.metadata.create_all(db.bind)  # Recreate all tables


if __name__ == "__main__":
    init_db()
