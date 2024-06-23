# app/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        os.environ['OPENAI_API_KEY'] = self.openai_api_key

        if os.getenv('OPENAI_API_KEY') is None:
            raise ValueError('OPENAI_API_KEY is not set in environment variable')

settings = Settings()


