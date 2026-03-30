from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/cabs",
    tags=["cabs"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Cab)
def create_cab(cab: schemas.CabCreate, db: Session = Depends(get_db)):
    db_cab = models.Cab(**cab.dict())
    db.add(db_cab)
    db.commit()
    db.refresh(db_cab)
    return db_cab

@router.get("/", response_model=List[schemas.Cab])
def read_cabs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cabs = db.query(models.Cab).offset(skip).limit(limit).all()
    return cabs

@router.get("/{cab_id}", response_model=schemas.Cab)
def read_cab(cab_id: int, db: Session = Depends(get_db)):
    cab = db.query(models.Cab).filter(models.Cab.id == cab_id).first()
    if cab is None:
        raise HTTPException(status_code=404, detail="Cab not found")
    return cab
