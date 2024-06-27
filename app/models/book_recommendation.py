from pydantic import BaseModel, validator, ValidationError

class BookRecommendationRequest(BaseModel):
    user_input: str

    @validator('user_input')
    def user_input_min_length(cls, v):
        if len(v) < 3:
            raise ValueError('user_input must be at least 3 characters long')
        return v


class BookRecommendationResponse(BaseModel):
    title: str
    author: str
    description: str
    suitable_for: str
    bullet_points: list[str]