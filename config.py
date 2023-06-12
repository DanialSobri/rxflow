import os
from dotenv import load_dotenv
import secrets
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str = "rxflow"
    FAKE:bool = True
    WSTOKEN:str = os.getenv('WSTOKEN')

    class Config:
        case_sensitive = True


settings = Settings()

