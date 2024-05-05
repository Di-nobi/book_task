import unittest
from fastapi.testclient import TestClient
from api.main import my_app
from fastapi.testclient import TestClient

client = TestClient(my_app)

def test_create_book():
    response = client.post("/books", json={"title": "Test Book", "author": "Test Author"})
    assert response.status_code == 200

def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_book():
    response = client.put("/books/1", json={"title": "Updated Title", "author": "Updated Author"})
    assert response.status_code == 200

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"


if __name__ == '__main__':
    unittest.main()