from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = "Passenger"

class UserCreate(UserBase):
    password: str

class UserUpdateRole(BaseModel):
    role: str

class User(UserBase):
    id: str
    created_at: datetime

    model_config = {"from_attributes": True}

class CabBase(BaseModel):
    license_plate: str
    driver_id: Optional[str] = None
    current_location: Optional[str] = None
    status: str = "Available"
    vehicle_class: Optional[str] = None

class CabCreate(CabBase):
    pass

class Cab(CabBase):
    id: str
    created_at: datetime

    model_config = {"from_attributes": True}

class BookingBase(BaseModel):
    user_id: str
    cab_id: Optional[str] = None
    pickup_location: str
    dropoff_location: str
    status: str = "Pending"
    fare: Optional[float] = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: str
    created_at: datetime
    assigned_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class TransactionBase(BaseModel):
    booking_id: str
    amount: float
    currency: str = "GBP"
    payment_method: Optional[str] = None
    status: str = "Pending"

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: str
    transaction_date: datetime

    model_config = {"from_attributes": True}

class ReportBase(BaseModel):
    report_type: str
    data: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: str
    generated_at: datetime

    model_config = {"from_attributes": True}
