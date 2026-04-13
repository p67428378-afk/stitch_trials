from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app import models, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.post("/", response_model=schemas.Transaction, status_code=status.HTTP_200_OK)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_booking = db.query(models.Booking).filter(models.Booking.id == transaction.booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")

    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/", response_model=List[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions

@router.get("/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(transaction_id: str, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.put("/{transaction_id}/status", response_model=schemas.Transaction)
def update_transaction_status(transaction_id: str, status: str, db: Session = Depends(get_db)):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db_transaction.status = status
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
