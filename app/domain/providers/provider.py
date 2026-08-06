from abc import ABC, abstractmethod

from app.domain.entities.chat_result import ChatResult


class LLMProvider(ABC):
    """
    Contract implemented by every LLM provider.
    """

    @abstractmethod
    async def chat(
        self,
        prompt: str,
    ) -> ChatResult:
        """
        Generate a chat completion.
        """
        raise NotImplementedError
