from database_session import get_db
from models import *
from database_session import Base

# Database initialization
def init_db():
    with get_db() as db:
        Base.metadata.drop_all(db.bind)    # Drop all tables
        Base.metadata.create_all(db.bind)  # Recreate all tables

if __name__ == "__main__":
    init_db()
