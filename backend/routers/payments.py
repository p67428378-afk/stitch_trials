from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["payments"],
    responses={404: {"description": "Not found"}},
)

@router.get("/summary")
def get_financial_summary():
    # Mock data for financial summary
    return {
        "total_revenue": 142500.00
    }

@router.get("/transactions", response_model=list[schemas.Transaction])
def get_recent_transactions(db: Session = Depends(get_db)):
    # Mock data for recent transactions
    # In a real app, this would query the database
    return [
        schemas.Transaction(id=1, booking_id=101, amount=42.50, currency="GBP", status="completed", created_at="2023-01-01T12:00:00"),
        schemas.Transaction(id=2, booking_id=102, amount=18.00, currency="GBP", status="completed", created_at="2023-01-01T12:05:00"),
        schemas.Transaction(id=3, booking_id=103, amount=312.45, currency="GBP", status="pending", created_at="2023-01-01T12:10:00"),
        schemas.Transaction(id=4, booking_id=104, amount=22.00, currency="GBP", status="failed", created_at="2023-01-01T12:15:00"),
    ]

@router.post("/initiate")
def initiate_payment(payment_details: dict):
    # Mock payment initiation
    return {"message": "Payment initiated successfully"}
