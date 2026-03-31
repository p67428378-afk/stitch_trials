import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_kpis(client):
    response = client.get("/analytics/kpis")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "total_rides" in response.json()
    assert "active_drivers" in response.json()
    assert "avg_wait_time" in response.json()

def test_get_driver_performance(client):
    response = client.get("/analytics/driver_performance")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
