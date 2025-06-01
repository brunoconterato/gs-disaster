from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
host=os.getenv("HOST")
dbname=os.getenv("DATABASE")
user=os.getenv("USER")
password=os.getenv("PASSWORD")
port=os.getenv("PORT")

# Gera a URL de conexão
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Create tables if they don't exist.  Only run this once!  Move this to init_db.py
#Base.metadata.create_all(engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
