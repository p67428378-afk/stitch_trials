import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_booking(client):
    response = client.post(
        "/bookings/",
        json={
            "pickup_location": "Central Station",
            "dropoff_location": "LHR Airport T5",
            "passenger_name": "John Doe",
            "vehicle_class": "Premium Sedan"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["pickup_location"] == "Central Station"
    assert data["dropoff_location"] == "LHR Airport T5"
    assert data["passenger_name"] == "John Doe"
    assert data["vehicle_class"] == "Premium Sedan"
    assert data["status"] == "pending"

def test_get_pending_dispatches(client):
    response = client.get("/bookings/pending")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
