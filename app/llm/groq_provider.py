from langchain_groq import ChatGroq

from app.core.config import settings

class GroqProvider:

    @staticmethod
    def create(model: str, temperature: float):

        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY não encontrada no ambiente.")

        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=model,
            temperature=temperature,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )