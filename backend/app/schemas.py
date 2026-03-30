from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional
from enum import Enum

class UserRole(str, Enum):
    passenger = "Passenger"
    driver = "Driver"
    dispatcher = "Dispatcher"
    administrator = "Administrator"

class UserBase(BaseModel):
    email: EmailStr
    role: UserRole # Use Enum for role validation

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class CabBase(BaseModel):
    driver_id: int
    license_plate: str
    model: str
    status: Optional[str] = "available"

class CabCreate(CabBase):
    pass

class Cab(CabBase):
    id: int

    class Config:
        from_attributes = True

class PaymentBase(BaseModel):
    user_id: int
    amount: float
    currency: Optional[str] = "USD"
    status: Optional[str] = "pending"

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class ReportBase(BaseModel):
    title: str
    content: str
    report_type: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int
    generated_at: datetime

    class Config:
        from_attributes = True

class TrackingBase(BaseModel):
    cab_id: int
    latitude: float
    longitude: float
    timestamp: datetime

class TrackingCreate(TrackingBase):
    pass

class Tracking(TrackingBase):
    id: int

    class Config:
        from_attributes = True
