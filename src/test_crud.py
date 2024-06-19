from fastapi.testclient import TestClient
import pytest
from main import app
from routers import *
import warnings


@pytest.fixture(scope="module")
def client():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    with TestClient(app) as test_client:
        yield test_client


def test_status(client):
    response = client.get("http://0.0.0.0:8000/document/api/")

    assert response.status_code == 200
    assert response.json() == {"status": True}


def test_upload(client):
    with open("/app/image.png", "rb") as file:
        response = client.post(
            "http://0.0.0.0:8000/document/document/",
            files={"data": file, "type": "image/png"},
        )

    assert response.status_code == 200
    assert response.json() == "/app/Documents/image.png"
