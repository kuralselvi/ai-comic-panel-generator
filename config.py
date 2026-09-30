from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Comic Craft AI"
    gemini_api_key: str = ""
    model_config = {"extra": "allow"}

@lru_cache
def get_settings():
    return Settings()

settings = Settings()