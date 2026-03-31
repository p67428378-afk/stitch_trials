from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="passenger")
    is_active = Column(Boolean, default=True)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    pickup_location = Column(String)
    dropoff_location = Column(String)
    passenger_name = Column(String)
    vehicle_class = Column(String)
    status = Column(String, default="pending") # pending, assigned, completed, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    assigned_driver_id = Column(Integer, nullable=True)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, index=True)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String, default="pending") # pending, completed, failed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
