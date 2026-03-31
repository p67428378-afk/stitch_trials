import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app import models, schemas


def test_create_booking(client: TestClient, db_session: Session):
    # Create a user first
    user_data = {
        "username": "bookinguser",
        "email": "booking@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Central Station",
        "dropoff_location": "LHR Airport T5",
        "fare": 50.00
    }
    response = client.post("/bookings/", json=booking_data)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["pickup_location"] == "Central Station"
    assert data["status"] == "Pending"
    assert "id" in data

    booking = db_session.query(models.Booking).filter(models.Booking.id == data["id"]).first()
    assert booking is not None


def test_get_bookings(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "bookinguser2",
        "email": "booking2@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location X",
        "dropoff_location": "Location Y",
        "fare": 20.00
    }
    client.post("/bookings/", json=booking_data)

    response = client.get("/bookings/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(b["user_id"] == user_id for b in data)


def test_get_pending_bookings(client: TestClient, db_session: Session):
    # Create a user and pending booking
    user_data = {
        "username": "bookinguser3",
        "email": "booking3@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location P",
        "dropoff_location": "Location Q",
        "status": "Pending",
        "fare": 30.00
    }
    client.post("/bookings/", json=booking_data)

    # Create a completed booking (should not appear in pending)
    user_data_2 = {
        "username": "bookinguser4",
        "email": "booking4@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response_2 = client.post("/users/", json=user_data_2)
    user_id_2 = user_response_2.json()["id"]

    booking_data_2 = {
        "user_id": user_id_2,
        "pickup_location": "Location R",
        "dropoff_location": "Location S",
        "status": "Completed",
        "fare": 40.00
    }
    client.post("/bookings/", json=booking_data_2)

    response = client.get("/bookings/pending")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(b["user_id"] == user_id and b["status"] == "Pending" for b in data)
    assert not any(b["user_id"] == user_id_2 for b in data)


def test_get_booking(client: TestClient, db_session: Session):
    # Create a user and booking first
    user_data = {
        "username": "bookinguser5",
        "email": "booking5@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    booking_data = {
        "user_id": user_id,
        "pickup_location": "Location M",
        "dropoff_location": "Location N",
        "fare": 10.00
    }
    post_response = client.post("/bookings/", json=booking_data)
    booking_id = post_response.json()["id"]

    response = client.get(f"/bookings/{booking_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == booking_id


def test_assign_cab_to_booking(client: TestClient, db_session: Session):
    # Create a user
    user_data = {
        "username": "bookinguser6",
        "email": "booking6@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    # Create a cab
    cab_data = {
        "license_plate": "CAB123",
        "vehicle_class": "Standard"
    }
    cab_response = client.post("/cabs/", json=cab_data)
    cab_id = cab_response.json()["id"]

    # Create a booking
    booking_data = {
        "user_id": user_id,
        "pickup_location": "Start",
        "dropoff_location": "End",
        "fare": 25.00
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    response = client.put(f"/bookings/{booking_id}/assign/{cab_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["cab_id"] == cab_id
    assert data["status"] == "Assigned"
    assert "assigned_at" in data

    booking = db_session.query(models.Booking).filter(models.Booking.id == booking_id).first()
    assert booking.cab_id == cab_id
    assert booking.status == "Assigned"


def test_complete_booking(client: TestClient, db_session: Session):
    # Create a user
    user_data = {
        "username": "bookinguser7",
        "email": "booking7@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    # Create a booking
    booking_data = {
        "user_id": user_id,
        "pickup_location": "Start",
        "dropoff_location": "End",
        "fare": 25.00
    }
    booking_response = client.post("/bookings/", json=booking_data)
    booking_id = booking_response.json()["id"]

    response = client.put(f"/bookings/{booking_id}/complete")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Completed"
    assert "completed_at" in data

    booking = db_session.query(models.Booking).filter(models.Booking.id == booking_id).first()
    assert booking.status == "Completed"
