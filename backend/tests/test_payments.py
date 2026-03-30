import pytest
from app.models import Payment

def test_create_payment(client, session):
    response = client.post(
        "/payments/",
        json={"user_id": 1, "amount": 25.50, "currency": "USD", "status": "completed"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 25.50
    assert data["currency"] == "USD"
    assert data["status"] == "completed"
    assert "id" in data

    payment = session.query(Payment).filter(Payment.user_id == 1).first()
    assert payment is not None
    assert payment.amount == 25.50

def test_read_payments(client, session):
    client.post(
        "/payments/",
        json={"user_id": 1, "amount": 10.00, "currency": "USD", "status": "pending"}
    )
    client.post(
        "/payments/",
        json={"user_id": 2, "amount": 30.00, "currency": "EUR", "status": "completed"}
    )
    response = client.get("/payments/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["amount"] == 10.00
    assert data[1]["amount"] == 30.00
