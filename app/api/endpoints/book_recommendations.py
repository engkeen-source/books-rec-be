from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.book import BookRecommendationRequest, BookRecommendationResponse
from app.services.book_recommendation import recommend_books

router = APIRouter()

@router.post("/recommend", response_model=List[BookRecommendationResponse])
def get_book_recommendation(request: BookRecommendationRequest):
    try:
        return recommend_books(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
