from database_session import get_db
from models import *
from database_session import Base
from sqlalchemy import text


# Database initialization
def init_db():
    with get_db() as db:
        with db.bind.connect() as conn:
            conn.execute(
                text("DROP VIEW IF EXISTS resampled_measurements_daily CASCADE;")
            )
            conn.commit()
        Base.metadata.drop_all(db.bind)  # Drop all tables
        Base.metadata.create_all(db.bind)  # Recreate all tables


if __name__ == "__main__":
    init_db()
