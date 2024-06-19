from fastapi.testclient import TestClient
import pytest
from main import app
from routers import *


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_upload(client):
    with open("/app/image.png", "rb") as file:
        response = client.post(
            "http://localhost:8000/document/document/",
            headers={
                "accept": "application/json",
                "Content-Type": "multipart/form-data",
            },
            files={"data": file, "type": "image/png"},
        )

    assert response.json() == {"detail": "/app/Documents/image.png"}
    assert response.status_code == 202


def test_status(client):
    response = client.get("http://localhost:8000/document/api/")

    assert response.status_code == 200
    assert response.json() == {"status": True}
