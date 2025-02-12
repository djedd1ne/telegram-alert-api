import pytest
from wsgi import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

#Valid notification
def test_valid_notification(client):
    response = client.post("/notify", json={
        "Type": "Warning",
        "Name": "Backup Failure",
        "Description": "The backup failed due to a database problem"
    })
    assert response.status_code == 200
    assert response.json == {"The backup failed due to a database problem": "OK"}

#Invalid notification
def test_invalid_notification(client):
    response = client.post("/notify", json={
        "Type": "Warning!",
        "Name": "CPU#Overload",
        "Description": "Invalid Input"
    })
    assert response.status_code == 400

#Missing fields
def test_missing_fields(client):
    response = client.post("/notify", json={
        "Name": "CPU",
        "Description": "Missing Type Field"
    })
    assert response.status_code == 400

#Get notifications
def test_get_notifications(client):
    response = client.get("/notifications")
    assert response.status_code == 200
    assert isinstance(response.json, list)
