import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../db')))

# from sqlalchemy.orm import declarative_base
from db.database_session import get_db  # Import get_db function
from db.models import *
from db.database_session import Base
from sqlalchemy import text

# Database initialization
def init_db():
    with get_db() as db:
        Base.metadata.create_all(db.bind)       

if __name__ == "__main__":
    init_db()
