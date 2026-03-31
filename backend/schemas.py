from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role: str = "passenger"

class User(UserBase):
    id: int
    is_active: bool
    role: str

    model_config = ConfigDict(from_attributes=True)

class BookingBase(BaseModel):
    pickup_location: str
    dropoff_location: str
    passenger_name: str
    vehicle_class: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    status: str
    created_at: datetime
    assigned_driver_id: int | None = None

    model_config = ConfigDict(from_attributes=True)

class TransactionBase(BaseModel):
    booking_id: int
    amount: float
    currency: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
