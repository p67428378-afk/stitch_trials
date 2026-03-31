import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app import models, schemas


def test_create_transaction(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "paymentuser",
        "email": "payment@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location A",
        "dropoff_location": "Location B",
        "fare": 25.50
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    transaction_data = {
        "booking_id": booking_id,
        "amount": 25.50,
        "payment_method": "Credit Card"
    }
    response = client.post("/payments/", json=transaction_data)
    assert response.status_code == 200
    data = response.json()
    assert data["booking_id"] == booking_id
    assert data["amount"] == 25.50
    assert data["payment_method"] == "Credit Card"
    assert "id" in data

    transaction = db_session.query(models.Transaction).filter(models.Transaction.id == data["id"]).first()
    assert transaction is not None


def test_get_transactions(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "paymentuser2",
        "email": "payment2@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location C",
        "dropoff_location": "Location D",
        "fare": 30.00
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    transaction_data = {
        "booking_id": booking_id,
        "amount": 30.00,
        "payment_method": "Mobile Wallet"
    }
    client.post("/payments/", json=transaction_data)

    response = client.get("/payments/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(t["booking_id"] == booking_id for t in data)


def test_get_transaction(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "paymentuser3",
        "email": "payment3@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location E",
        "dropoff_location": "Location F",
        "fare": 15.00
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    transaction_data = {
        "booking_id": booking_id,
        "amount": 15.00,
        "payment_method": "In-App"
    }
    post_response = client.post("/payments/", json=transaction_data)
    transaction_id = post_response.json()["id"]

    response = client.get(f"/payments/{transaction_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["booking_id"] == booking_id


def test_update_transaction_status(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "paymentuser4",
        "email": "payment4@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location G",
        "dropoff_location": "Location H",
        "fare": 50.00
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    transaction_data = {
        "booking_id": booking_id,
        "amount": 50.00,
        "payment_method": "Credit Card",
        "status": "Pending"
    }
    post_response = client.post("/payments/", json=transaction_data)
    transaction_id = post_response.json()["id"]

    new_status = "Completed"
    response = client.put(f"/payments/{transaction_id}/status?status={new_status}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == new_status

    transaction = db_session.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    assert transaction.status == new_status
