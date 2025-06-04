from database_session import get_db
from models import *
from database_session import Base


# Database initialization
def init_db():
    with get_db() as db:
        Base.metadata.create_all(db.bind)


if __name__ == "__main__":
    init_db()
