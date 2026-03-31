from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = models.Booking(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/pending", response_model=list[schemas.Booking])
def get_pending_dispatches(db: Session = Depends(get_db)):
    return db.query(models.Booking).filter(models.Booking.status == "pending").all()

@router.post("/{booking_id}/assign/{driver_id}", response_model=schemas.Booking)
def assign_driver_to_booking(booking_id: int, driver_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db_booking.assigned_driver_id = driver_id
    db_booking.status = "assigned"
    db.commit()
    db.refresh(db_booking)
    return db_booking
