import os
from pydantic import BaseSettings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
class Settings(BaseSettings):
    MONGODB_URL: str = os.getenv('DB_URL')
    MONGODB_NAME: str = os.getenv('DB_NAME')
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    
settings = Settings()