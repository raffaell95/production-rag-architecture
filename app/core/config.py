import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.getenv("REDIS_DB", 0))
    HISTORY_TTL: int = int(os.getenv("HISTORY_TTL", 60*60*24))

    # LLM / GROQ
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

settings = Settings()