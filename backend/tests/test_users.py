import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app.main import app
from backend.app import models
from backend.app import schemas


def test_create_user(client: TestClient, db_session: Session):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword",
        "role": "Passenger"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["role"] == "Passenger"
    assert "id" in data
    assert "created_at" in data

    # Verify user is in the database
    user = db_session.query(models.User).filter(models.User.email == "test@example.com").first()
    assert user is not None
    assert user.username == "testuser"


def test_get_users(client: TestClient, db_session: Session):
    # Create a user first
    user_data = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "securepassword2",
        "role": "Driver"
    }
    client.post("/users/", json=user_data)

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert any(user["email"] == "test2@example.com" for user in data)


def test_get_user(client: TestClient, db_session: Session):
    user_data = {
        "username": "testuser3",
        "email": "test3@example.com",
        "password": "securepassword3",
        "role": "Dispatcher"
    }
    post_response = client.post("/users/", json=user_data)
    user_id = post_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser3"
    assert data["email"] == "test3@example.com"


def test_update_user_role(client: TestClient, db_session: Session):
    user_data = {
        "username": "testuser4",
        "email": "test4@example.com",
        "password": "securepassword4",
        "role": "Passenger"
    }
    post_response = client.post("/users/", json=user_data)
    user_id = post_response.json()["id"]

    update_data = {"role": "Driver"}
    response = client.put(f"/users/{user_id}/role", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "Driver"

    # Verify role updated in DB
    user = db_session.query(models.User).filter(models.User.id == user_id).first()
    assert user.role == "Driver"
