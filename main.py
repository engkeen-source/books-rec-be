from fastapi import FastAPI

from app.middleware import setup_middleware  # Import the middleware setup function
from app.api.endpoints import book_recommendations
from app.config import settings

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)  # turn off swagger docs

setup_middleware(app)

app.include_router(book_recommendations.router, prefix="/books", tags=["books"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Recommendation System"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
