import pytest
from fastapi.testclient import TestClient
from app.api.endpoints.book_cover import router
from app.models.book_cover import BookCoverRequest, BookCoverResponse

client = TestClient(router)

@pytest.fixture
def book_cover_request():
    return BookCoverRequest(
        title= "The Lean Startup",
        author= "Eric Ries"
    )

def test_get_book_cover(book_cover_request):
    response = client.post("/cover", json=book_cover_request.dict())
    assert response.status_code == 200
    response_data = response.json()
    assert BookCoverResponse(**response_data)