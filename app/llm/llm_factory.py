from dotenv import load_dotenv
from app.llm.groq_provider import GroqProvider


class LLMFactory:

    @staticmethod
    def create(provider: str, model: str, temperature: float = 0.2):
        load_dotenv()

        if provider == "groq":
            return GroqProvider.create(model, temperature)

        raise ValueError(f"Provider {provider} não suportado.")