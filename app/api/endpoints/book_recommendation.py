from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models.book_recommendation import BookRecommendationRequest, BookRecommendationResponse
from app.services.book_recommendation import get_books_from_openai

router = APIRouter()

@router.post("/recommend", response_model=List[BookRecommendationResponse])
def get_book_recommendation(request: BookRecommendationRequest):
    try:
        return get_books_from_openai(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
