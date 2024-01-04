from fastapi.testclient import TestClient
from jsecurity_service import app

client = TestClient(app)
