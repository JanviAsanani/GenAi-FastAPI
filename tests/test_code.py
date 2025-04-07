from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_code_file():
    response = client.post("/code/", json={"id": 1, "content": "print('Hello')", "owner_id": 1})
    assert response.status_code == 200
    assert response.json()["id"] == 1