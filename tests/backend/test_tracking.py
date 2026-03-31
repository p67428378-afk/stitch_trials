import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_live_operations(client):
    response = client.get("/tracking/live")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "active_units" in response.json()
    assert "zone_alert" in response.json()

def test_get_ride_progress(client):
    response = client.get("/tracking/progress")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
