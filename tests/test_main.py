from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book Recommendation System"}


def test_book_recommendation():
    response = client.post(
        "/books/recommend", json={"user_input": "I like science fiction"}
    )
    assert response.status_code == 200
    assert "recommendations" in response.json()
