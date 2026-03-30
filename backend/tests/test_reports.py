import pytest
from app.models import Report

def test_create_report(client, session):
    response = client.post(
        "/reports/",
        json={"title": "Monthly Revenue Report", "content": "Total revenue: $10000", "report_type": "financial"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Monthly Revenue Report"
    assert data["report_type"] == "financial"
    assert "id" in data

    report = session.query(Report).filter(Report.title == "Monthly Revenue Report").first()
    assert report is not None
    assert report.content == "Total revenue: $10000"

def test_read_reports(client, session):
    client.post(
        "/reports/",
        json={"title": "Driver Performance Q1", "content": "Top driver: John Doe", "report_type": "performance"}
    )
    client.post(
        "/reports/",
        json={"title": "Customer Feedback Summary", "content": "Positive feedback: 80%", "report_type": "feedback"}
    )
    response = client.get("/reports/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Driver Performance Q1"
    assert data[1]["title"] == "Customer Feedback Summary"
