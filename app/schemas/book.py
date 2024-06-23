from typing import Optional
from pydantic import BaseModel, HttpUrl


class BookRecommendationRequest(BaseModel):
    user_input: str

class BookRecommendationResponse(BaseModel):
    title: str
    author: str
    description: str
    suitable_for: str
    bullet_points: list[str]
    cover_image_url: Optional[HttpUrl] = None  # Add cover image URL to the response model with a default value of None

class BookCoverRequest(BaseModel):
    title: str
    author: str

class BookCoverResponse(BaseModel):
    cover_url: HttpUrl


