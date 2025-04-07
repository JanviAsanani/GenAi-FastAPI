from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Hello")
        response = websocket.receive_text()
        assert response == "Echo: Hello"