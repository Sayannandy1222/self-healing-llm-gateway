from app.domain.providers.provider import LLMProvider
from app.infrastructure.providers.groq_provider import GroqProvider


class ProviderRegistry:
    """
    Provider registry.
    """

    @staticmethod
    def get_default_provider() -> LLMProvider:
        return GroqProvider()