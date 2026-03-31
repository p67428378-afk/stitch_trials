import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_financial_summary(client):
    response = client.get("/payments/summary")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "total_revenue" in response.json()

def test_get_recent_transactions(client):
    response = client.get("/payments/transactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_initiate_payment(client):
    response = client.post("/payments/initiate", json={"amount": 50.00, "currency": "GBP"})
    assert response.status_code == 200
    assert response.json() == {"message": "Payment initiated successfully"}
