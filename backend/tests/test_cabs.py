import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app import models, schemas


def test_create_cab(client: TestClient, db_session: Session):
    cab_data = {
        "license_plate": "TEST123",
        "vehicle_class": "Premium Sedan"
    }
    response = client.post("/cabs/", json=cab_data)
    assert response.status_code == 200
    data = response.json()
    assert data["license_plate"] == "TEST123"
    assert data["vehicle_class"] == "Premium Sedan"
    assert "id" in data

    cab = db_session.query(models.Cab).filter(models.Cab.license_plate == "TEST123").first()
    assert cab is not None


def test_get_cabs(client: TestClient, db_session: Session):
    cab_data = {
        "license_plate": "TEST456",
        "vehicle_class": "Electric Eco"
    }
    client.post("/cabs/", json=cab_data)

    response = client.get("/cabs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert any(cab["license_plate"] == "TEST456" for cab in data)


def test_get_cab(client: TestClient, db_session: Session):
    cab_data = {
        "license_plate": "TEST789",
        "vehicle_class": "MPV 7-Seater"
    }
    post_response = client.post("/cabs/", json=cab_data)
    cab_id = post_response.json()["id"]

    response = client.get(f"/cabs/{cab_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["license_plate"] == "TEST789"


def test_assign_cab_to_driver(client: TestClient, db_session: Session):
    # Create a driver
    driver_data = {
        "username": "testdriver",
        "email": "driver@example.com",
        "password": "driverpass",
        "role": "Driver"
    }
    driver_response = client.post("/users/", json=driver_data)
    driver_id = driver_response.json()["id"]

    # Create a cab
    cab_data = {
        "license_plate": "ASSIGN1",
        "vehicle_class": "Sedan"
    }
    cab_response = client.post("/cabs/", json=cab_data)
    cab_id = cab_response.json()["id"]

    response = client.put(f"/cabs/{cab_id}/assign/{driver_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["driver_id"] == driver_id

    cab = db_session.query(models.Cab).filter(models.Cab.id == cab_id).first()
    assert cab.driver_id == driver_id


def test_update_cab_location(client: TestClient, db_session: Session):
    cab_data = {
        "license_plate": "LOCATION1",
        "vehicle_class": "Hatchback"
    }
    cab_response = client.post("/cabs/", json=cab_data)
    cab_id = cab_response.json()["id"]

    new_location = "51.5074,0.1278"
    response = client.put(f"/cabs/{cab_id}/location?location={new_location}")
    assert response.status_code == 200
    data = response.json()
    assert data["current_location"] == new_location

    cab = db_session.query(models.Cab).filter(models.Cab.id == cab_id).first()
    assert cab.current_location == new_location
