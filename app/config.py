# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    canvas_base_url: str
    canvas_token: str

    class Config:
        env_file = ".env"

settings = Settings()