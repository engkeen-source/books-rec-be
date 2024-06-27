from pydantic import BaseModel, HttpUrl

class BookCoverRequest(BaseModel):
    title: str
    author: str

class BookCoverResponse(BaseModel):
    cover_url: HttpUrl


