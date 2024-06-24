import os
import requests
from typing import Optional

from app.schemas.book import BookCoverRequest, BookCoverResponse


def get_book_cover(request: BookCoverRequest) -> Optional[BookCoverResponse]:

    GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'
    GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')

    params = {
        'q': f'intitle:{request.title}+inauthor:{request.author}',
        'key': GOOGLE_BOOKS_API_KEY
    }

    try:
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch data from Google Books API: {e}")

    data = response.json()
    items = data.get('items', [])

    if not items:
        return None

    book_info = items[0].get('volumeInfo', {})
    image_links = book_info.get('imageLinks', {})

    cover_url = image_links.get('thumbnail')
    
    if cover_url:
        return BookCoverResponse(cover_url=cover_url)
    return None

# Example usage
if __name__ == "__main__":
    cover_request = BookCoverRequest(title="To Kill a Mockingbird", author="Harper Lee")
    cover_url = get_book_cover(cover_request)
    print(cover_url)
