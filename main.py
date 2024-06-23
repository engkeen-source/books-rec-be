from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import book_recommendations

from app.config import settings

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", 
                   "https://bookrecommend.app"
                   "https://www.bookrecommend.app"
                   ],
    allow_origin_regex="http://192.168.1.*",  # Allow all 192.168.1.* IPs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
app.include_router(book_recommendations.router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Recommendation System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app"
    )