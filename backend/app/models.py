from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base # Import Base from database.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="Passenger") # Added role field

    payments = relationship("Payment", back_populates="owner")

class Cab(Base):
    __tablename__ = "cabs"

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, index=True) # Assuming driver_id links to a User
    license_plate = Column(String, unique=True, index=True)
    model = Column(String)
    status = Column(String, default="available") # e.g., available, enroute, occupied

    tracking_entries = relationship("Tracking", back_populates="cab")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    currency = Column(String, default="USD")
    status = Column(String, default="pending") # e.g., pending, completed, failed
    timestamp = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="payments")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    report_type = Column(String) # e.g., financial, performance, feedback
    generated_at = Column(DateTime, default=datetime.utcnow)

class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True, index=True)
    cab_id = Column(Integer, ForeignKey("cabs.id"))
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    cab = relationship("Cab", back_populates="tracking_entries")
