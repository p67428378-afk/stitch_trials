import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app import models, schemas


def test_get_all_cab_locations(client: TestClient, db_session: Session):
    # Create a driver
    driver_data = {
        "username": "driver1",
        "email": "driver1@example.com",
        "password": "securepassword",
        "role": "Driver"
    }
    driver_response = client.post("/users/", json=driver_data)
    driver_id = driver_response.json()["id"]

    # Create cabs with locations
    cab_data_1 = {
        "license_plate": "TRACK1",
        "driver_id": driver_id,
        "current_location": "51.5074,0.1278",
        "vehicle_class": "Standard"
    }
    client.post("/cabs/", json=cab_data_1)

    cab_data_2 = {
        "license_plate": "TRACK2",
        "driver_id": driver_id,
        "current_location": "51.5174,0.1378",
        "vehicle_class": "Premium"
    }
    client.post("/cabs/", json=cab_data_2)

    # Create a cab without location
    cab_data_3 = {
        "license_plate": "TRACK3",
        "driver_id": driver_id,
        "vehicle_class": "Economy"
    }
    client.post("/cabs/", json=cab_data_3)

    response = client.get("/tracking/cabs/location")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2  # Only cabs with current_location should be returned
    assert any(cab["license_plate"] == "TRACK1" for cab in data)
    assert any(cab["license_plate"] == "TRACK2" for cab in data)
    assert not any(cab["license_plate"] == "TRACK3" for cab in data)


def test_get_all_trip_progress(client: TestClient, db_session: Session):
    # Create a user
    user_data = {
        "username": "tripuser",
        "email": "trip@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    user_response = client.post("/users/", json=user_data)
    user_id = user_response.json()["id"]

    # Create a cab
    cab_data = {
        "license_plate": "TRIPCAB",
        "vehicle_class": "Standard"
    }
    cab_response = client.post("/cabs/", json=cab_data)
    cab_id = cab_response.json()["id"]

    # Create an in-progress booking
    booking_data_1 = {
        "user_id": user_id,
        "cab_id": cab_id,
        "pickup_location": "Start A",
        "dropoff_location": "End A",
        "status": "In-Progress",
        "fare": 10.00
    }
    client.post("/bookings/", json=booking_data_1)

    # Create another in-progress booking
    booking_data_2 = {
        "user_id": user_id,
        "cab_id": cab_id,
        "pickup_location": "Start B",
        "dropoff_location": "End B",
        "status": "In-Progress",
        "fare": 15.00
    }
    client.post("/bookings/", json=booking_data_2)

    # Create a completed booking (should not appear)
    booking_data_3 = {
        "user_id": user_id,
        "cab_id": cab_id,
        "pickup_location": "Start C",
        "dropoff_location": "End C",
        "status": "Completed",
        "fare": 20.00
    }
    client.post("/bookings/", json=booking_data_3)

    response = client.get("/tracking/trips/progress")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2  # Only in-progress trips should be returned
    assert any(booking["pickup_location"] == "Start A" for booking in data)
    assert any(booking["pickup_location"] == "Start B" for booking in data)
    assert not any(booking["pickup_location"] == "Start C" for booking in data)
