from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from backend.app.models import Base # Import Base from models.py

# Use environment variable for database URL, fallback to SQLite for local development
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    } if "sqlite" in SQLALCHEMY_DATABASE_URL else {},
    pool_pre_ping=True # For PostgreSQL, ensures connections are alive
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
