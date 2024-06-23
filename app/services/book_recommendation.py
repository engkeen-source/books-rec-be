import json
from openai import OpenAI
from typing import List
from app.schemas.book import BookRecommendationRequest, BookRecommendationResponse


def recommend_books(
    request: BookRecommendationRequest,
) -> List[BookRecommendationResponse]:

    user_prompt = f"""
        Return a list of books based on user input in the format of json. 
        You should include the title, author, description, suitable_for, and bullet_points fields.
        Each book should have the following fields:
        - title (string): The title of the book.
        - author (string): The author of the book.
        - description (string): A brief description of the book.
        - suitable_for (string): The user group who suitable to read this book, e.g. IT professionals, students, etc.
        - bullet_points (list of strings): A list of bullet points that summarize the book.
        The user input is: {request.user_input}
    """

    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "I want you to recommend best book based on user input.",
                },
                {"role": "user", "content": user_prompt},
            ],
        )
    except Exception as e:
        raise ValueError(f"Failed to get response from OpenAI: {e}")

    try:
        message_content = completion.choices[0].message.content
    except Exception as e:
        raise ValueError(
            f'Failed to extract "completion.choices[0].message.content": {e}'
        )

    # Get the 'books' from the response
    try:
        books_recommendations = json.loads(message_content)
        books_recommendations = books_recommendations.get("books", [])
    except json.JSONDecodeError:
        raise ValueError("Failed to parse response from OpenAI")

    return [BookRecommendationResponse(**book) for book in books_recommendations]
