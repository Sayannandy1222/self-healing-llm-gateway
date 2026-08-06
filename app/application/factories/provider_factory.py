from app.domain.providers.provider import LLMProvider
from app.infrastructure.providers.groq_provider import GroqProvider


class ProviderFactory:
    """
    Factory responsible for creating LLM provider implementations.
    """

    @staticmethod
    def create() -> LLMProvider:
        """
        Return the configured provider.
        """

        return GroqProvider()
