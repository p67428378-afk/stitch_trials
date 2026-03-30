import pytest
from app.models import User

def test_create_user(client, session):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "password123", "role": "Passenger"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["role"] == "Passenger"
    assert "id" in data
    assert "password" not in data

    # Verify user is in the database
    user = session.query(User).filter(User.email == "test@example.com").first()
    assert user is not None
    assert user.email == "test@example.com"

def test_create_user_invalid_role(client):
    response = client.post(
        "/users/",
        json={"email": "invalid@example.com", "password": "password123", "role": "InvalidRole"}
    )
    assert response.status_code == 422 # Unprocessable Entity for validation error

def test_read_users(client, session):
    client.post(
        "/users/",
        json={"email": "test1@example.com", "password": "password123", "role": "Passenger"}
    )
    client.post(
        "/users/",
        json={"email": "test2@example.com", "password": "password123", "role": "Driver"}
    )
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["email"] == "test1@example.com"
    assert data[1]["email"] == "test2@example.com"
