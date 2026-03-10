import pytest
from fastapi.testclient import TestClient
from app import app, tasks, next_id


@pytest.fixture(autouse=True)
def reset_state():
    """Limpa o estado antes de cada teste."""
    global next_id
    tasks.clear()
    import app as app_module
    app_module.next_id = 1
    yield


client = TestClient(app)


def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task():
    response = client.post("/tasks", json={"title": "Estudar FastAPI"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Estudar FastAPI"
    assert data["done"] is False
    assert data["id"] == 1


def test_create_task_missing_title():
    response = client.post("/tasks", json={})
    assert response.status_code == 422  # Validation error


def test_get_task_by_id():
    client.post("/tasks", json={"title": "Task X"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Task X"


def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task():
    client.post("/tasks", json={"title": "Antiga"})
    response = client.put("/tasks/1", json={"title": "Nova", "done": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Nova"
    assert data["done"] is True


def test_update_task_not_found():
    response = client.put("/tasks/999", json={"title": "X"})
    assert response.status_code == 404


def test_delete_task():
    client.post("/tasks", json={"title": "Deletar essa"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"


def test_delete_task_not_found():
    response = client.delete("/tasks/999")
    assert response.status_code == 404


def test_list_multiple_tasks():
    client.post("/tasks", json={"title": "T1"})
    client.post("/tasks", json={"title": "T2"})
    client.post("/tasks", json={"title": "T3"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 3