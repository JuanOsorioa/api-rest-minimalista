from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_obtener_tareas_vacia():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_crear_tarea():
    response = client.post("/tasks?tarea=Aprender DevOps")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Tarea creada"}