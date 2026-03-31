from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="Passenger") # e.g., Passenger, Driver, Dispatcher, Administrator
    created_at = Column(DateTime, default=datetime.utcnow)

    bookings = relationship("Booking", back_populates="user")
    driver_cabs = relationship("Cab", back_populates="driver")

class Cab(Base):
    __tablename__ = "cabs"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    license_plate = Column(String, unique=True, index=True, nullable=False)
    driver_id = Column(String, ForeignKey("users.id"), nullable=True) # Nullable if cab is unassigned
    current_location = Column(String, nullable=True) # e.g., "lat,long"
    status = Column(String, default="Available") # e.g., Available, On-Trip, Offline, Maintenance
    vehicle_class = Column(String, nullable=True) # e.g., Premium Sedan, MPV 7-Seater, Electric Eco
    created_at = Column(DateTime, default=datetime.utcnow)

    driver = relationship("User", back_populates="driver_cabs")
    bookings = relationship("Booking", back_populates="cab")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    cab_id = Column(String, ForeignKey("cabs.id"), nullable=True) # Nullable until assigned
    pickup_location = Column(String, nullable=False)
    dropoff_location = Column(String, nullable=False)
    status = Column(String, default="Pending") # e.g., Pending, Assigned, In-Progress, Completed, Cancelled
    fare = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    assigned_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="bookings")
    cab = relationship("Cab", back_populates="bookings")
    transactions = relationship("Transaction", back_populates="booking")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    booking_id = Column(String, ForeignKey("bookings.id"), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="GBP")
    payment_method = Column(String, nullable=True) # e.g., Credit Card, Mobile Wallet, In-App
    status = Column(String, default="Pending") # e.g., Pending, Completed, Failed, Refunded
    transaction_date = Column(DateTime, default=datetime.utcnow)

    booking = relationship("Booking", back_populates="transactions")

class Report(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    report_type = Column(String, nullable=False) # e.g., Daily, Weekly, Monthly, DriverPerformance
    generated_at = Column(DateTime, default=datetime.utcnow)
    data = Column(String) # Store report data as JSON string for simplicity
