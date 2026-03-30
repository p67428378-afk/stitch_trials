import pytest
from app.models import Cab

def test_create_cab(client, session):
    response = client.post(
        "/cabs/",
        json={"driver_id": 1, "license_plate": "XYZ-123", "model": "Sedan"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["license_plate"] == "XYZ-123"
    assert data["model"] == "Sedan"
    assert "id" in data

    cab = session.query(Cab).filter(Cab.license_plate == "XYZ-123").first()
    assert cab is not None
    assert cab.license_plate == "XYZ-123"

def test_read_cabs(client, session):
    client.post(
        "/cabs/",
        json={"driver_id": 1, "license_plate": "CAB-001", "model": "SUV"}
    )
    client.post(
        "/cabs/",
        json={"driver_id": 2, "license_plate": "CAB-002", "model": "Mini"}
    )
    response = client.get("/cabs/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["license_plate"] == "CAB-001"
    assert data[1]["license_plate"] == "CAB-002"
