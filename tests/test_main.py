from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "project": "Runner Factory"}

def test_list_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_read_doc_existing():
    response = client.get("/docs/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Protocolo de Seguridad Runner"

def test_read_doc_not_found():
    response = client.get("/docs/999")
    assert response.status_code == 404
