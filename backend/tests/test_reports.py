import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app import models, schemas


def test_create_report(client: TestClient, db_session: Session):
    report_data = {
        "report_type": "Daily",
        "data": "{\"total_rides\": 100, \"revenue\": 1500.00}"
    }
    response = client.post("/reports/", json=report_data)
    assert response.status_code == 200
    data = response.json()
    assert data["report_type"] == "Daily"
    assert "id" in data

    report = db_session.query(models.Report).filter(models.Report.id == data["id"]).first()
    assert report is not None


def test_read_reports(client: TestClient, db_session: Session):
    report_data = {
        "report_type": "Weekly",
        "data": "{\"total_rides\": 700, \"revenue\": 10500.00}"
    }
    client.post("/reports/", json=report_data)

    response = client.get("/reports/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(report["report_type"] == "Weekly" for report in data)


def test_read_report(client: TestClient, db_session: Session):
    report_data = {
        "report_type": "Monthly",
        "data": "{\"total_rides\": 3000, \"revenue\": 45000.00}"
    }
    post_response = client.post("/reports/", json=report_data)
    report_id = post_response.json()["id"]

    response = client.get(f"/reports/{report_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["report_type"] == "Monthly"
    assert data["id"] == report_id
