from pydantic import BaseModel, HttpUrl


class BookRecommendationRequest(BaseModel):
    user_input: str

class BookRecommendationResponse(BaseModel):
    title: str
    author: str
    description: str
    suitable_for: str
    bullet_points: list[str]


