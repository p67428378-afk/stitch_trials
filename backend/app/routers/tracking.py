from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/tracking",
    tags=["tracking"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Tracking)
def create_tracking_entry(tracking: schemas.TrackingCreate, db: Session = Depends(get_db)):
    db_tracking = models.Tracking(**tracking.dict())
    db.add(db_tracking)
    db.commit()
    db.refresh(db_tracking)
    return db_tracking

@router.get("/", response_model=List[schemas.Tracking])
def read_tracking_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tracking_entries = db.query(models.Tracking).offset(skip).limit(limit).all()
    return tracking_entries

@router.get("/{tracking_id}", response_model=schemas.Tracking)
def read_tracking_entry(tracking_id: int, db: Session = Depends(get_db)):
    tracking_entry = db.query(models.Tracking).filter(models.Tracking.id == tracking_id).first()
    if tracking_entry is None:
        raise HTTPException(status_code=404, detail="Tracking entry not found")
    return tracking_entry
