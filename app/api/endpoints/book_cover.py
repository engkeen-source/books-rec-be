
from fastapi import APIRouter, HTTPException
from app.models.book_cover import BookCoverRequest, BookCoverResponse

from app.services.book_cover import get_book_cover_from_google

router = APIRouter()

@router.post("/cover", response_model=BookCoverResponse)
def get_book_cover(request: BookCoverRequest):
    try:
        return get_book_cover_from_google(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))