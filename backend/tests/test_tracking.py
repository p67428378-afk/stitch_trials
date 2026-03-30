import pytest
from app.models import Tracking

def test_create_tracking_entry(client, session):
    response = client.post(
        "/tracking/",
        json={"cab_id": 1, "latitude": 34.0522, "longitude": -118.2437, "timestamp": "2023-10-27T10:00:00Z"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["cab_id"] == 1
    assert data["latitude"] == 34.0522
    assert data["longitude"] == -118.2437
    assert "id" in data

    tracking_entry = session.query(Tracking).filter(Tracking.cab_id == 1).first()
    assert tracking_entry is not None
    assert tracking_entry.latitude == 34.0522

def test_read_tracking_entries(client, session):
    client.post(
        "/tracking/",
        json={"cab_id": 1, "latitude": 34.0522, "longitude": -118.2437, "timestamp": "2023-10-27T10:00:00Z"}
    )
    client.post(
        "/tracking/",
        json={"cab_id": 2, "latitude": 34.0523, "longitude": -118.2438, "timestamp": "2023-10-27T10:01:00Z"}
    )
    response = client.get("/tracking/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["cab_id"] == 1
    assert data[1]["cab_id"] == 2
