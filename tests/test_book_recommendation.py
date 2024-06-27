import pytest
from fastapi.testclient import TestClient
from app.api.endpoints.book_recommendation import router
from app.models.book_recommendation import BookRecommendationRequest, BookRecommendationResponse
from pydantic import ValidationError

client = TestClient(router)

@pytest.fixture
def valid_book_recommendation_request():
    return BookRecommendationRequest(
        user_input="I like science fiction books with space adventures."
    )

def test_get_book_recommendation(valid_book_recommendation_request):
    response = client.post("/recommend", json=valid_book_recommendation_request.dict())
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0
    assert all(
        BookRecommendationResponse(**book_recommendation).dict() == book_recommendation
        for book_recommendation in response_data
    )