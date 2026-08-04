import pytest
from fastapi.testclient import TestClient


from backend.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_get_songs_valid_structure():
    response = client.get("/get_songs/relax")
    assert response.status_code == 200
    data = response.json()
    assert "mood" in data
    assert "songs" in data
    assert data["mood"] == "relax"
    assert isinstance(data["songs"], list)


def test_get_songs_unknown_mood():
    response = client.get("/get_songs/non_existent_mood_xyz")
    assert response.status_code == 200
    assert response.json() == {"mood": "non_existent_mood_xyz", "songs": []}