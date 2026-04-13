from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app import models, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/tracking",
    tags=["tracking"]
)

@router.get("/cabs/location", response_model=List[schemas.Cab])
def get_all_cab_locations(db: Session = Depends(get_db)):
    cabs = db.query(models.Cab).filter(models.Cab.current_location.isnot(None)).all()
    return cabs

@router.get("/trips/progress", response_model=List[schemas.Booking])
def get_all_trip_progress(db: Session = Depends(get_db)):
    trips_in_progress = db.query(models.Booking).filter(models.Booking.status == "In-Progress").all()
    return trips_in_progress
