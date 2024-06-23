# Book Recommendation System Backend

This is the backend for the Book Recommendation System, built with FastAPI.

## Project Structure

- `app/main.py`: The entry point of the application.
- `app/api/endpoints`: Contains API endpoint definitions.
- `app/models`: Contains database models (currently empty).
- `app/schemas`: Contains Pydantic models for request and response bodies.
- `app/services`: Contains business logic and service functions.
- `app/utils`: Contains utility functions.
- `tests`: Contains tests for the application.

## Running the Application

### With Docker

1. Build the Docker image:
    ```sh
    docker build -t book-recommendation-system-backend .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 80:80 book-recommendation-system-backend
    ```

### Without Docker

1. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 80
    ```

## Testing

Run the tests using pytest:
```sh
pytest
