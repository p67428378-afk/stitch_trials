from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from backend.app import models, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)

@router.post("/", response_model=schemas.Booking, status_code=status.HTTP_200_OK)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == booking.user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_booking = models.Booking(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/", response_model=List[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = db.query(models.Booking).offset(skip).limit(limit).all()
    return bookings

@router.get("/pending", response_model=List[schemas.Booking])
def read_pending_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pending_bookings = db.query(models.Booking).filter(models.Booking.status == "Pending").offset(skip).limit(limit).all()
    return pending_bookings

@router.get("/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: str, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.put("/{booking_id}/assign/{cab_id}", response_model=schemas.Booking)
def assign_cab_to_booking(booking_id: str, cab_id: str, db: Session = Depends(get_db)):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db_cab = db.query(models.Cab).filter(models.Cab.id == cab_id).first()
    if db_cab is None:
        raise HTTPException(status_code=404, detail="Cab not found")
    
    db_booking.cab_id = cab_id
    db_booking.status = "Assigned"
    db_booking.assigned_at = datetime.utcnow()
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.put("/{booking_id}/complete", response_model=schemas.Booking)
def complete_booking(booking_id: str, db: Session = Depends(get_db)):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    db_booking.status = "Completed"
    db_booking.completed_at = datetime.utcnow()
    db.commit()
    db.refresh(db_booking)
    return db_booking
