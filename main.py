from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import book_recommendation, book_cover
from app.config import settings

app = FastAPI() 


# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://bookrecommend.app",
        "https://www.bookrecommend.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(book_recommendation.router, tags=["books"])
app.include_router(book_cover.router, tags=["books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Recommendation System"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app")
