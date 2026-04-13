from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app import models, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/cabs",
    tags=["cabs"]
)

@router.post("/", response_model=schemas.Cab, status_code=status.HTTP_200_OK)
def create_cab(cab: schemas.CabCreate, db: Session = Depends(get_db)):
    db_cab = db.query(models.Cab).filter(models.Cab.license_plate == cab.license_plate).first()
    if db_cab:
        raise HTTPException(status_code=400, detail="Cab with this license plate already registered")
    db_cab = models.Cab(**cab.model_dump())
    db.add(db_cab)
    db.commit()
    db.refresh(db_cab)
    return db_cab

@router.get("/", response_model=List[schemas.Cab])
def read_cabs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cabs = db.query(models.Cab).offset(skip).limit(limit).all()
    return cabs

@router.get("/{cab_id}", response_model=schemas.Cab)
def read_cab(cab_id: str, db: Session = Depends(get_db)):
    cab = db.query(models.Cab).filter(models.Cab.id == cab_id).first()
    if cab is None:
        raise HTTPException(status_code=404, detail="Cab not found")
    return cab

@router.put("/{cab_id}/assign/{driver_id}", response_model=schemas.Cab)
def assign_cab_to_driver(cab_id: str, driver_id: str, db: Session = Depends(get_db)):
    db_cab = db.query(models.Cab).filter(models.Cab.id == cab_id).first()
    if db_cab is None:
        raise HTTPException(status_code=404, detail="Cab not found")
    db_driver = db.query(models.User).filter(models.User.id == driver_id, models.User.role == "Driver").first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found or user is not a driver")
    
    db_cab.driver_id = driver_id
    db.commit()
    db.refresh(db_cab)
    return db_cab

@router.put("/{cab_id}/location", response_model=schemas.Cab)
def update_cab_location(cab_id: str, location: str, db: Session = Depends(get_db)):
    db_cab = db.query(models.Cab).filter(models.Cab.id == cab_id).first()
    if db_cab is None:
        raise HTTPException(status_code=404, detail="Cab not found")
    db_cab.current_location = location
    db.commit()
    db.refresh(db_cab)
    return db_cab
