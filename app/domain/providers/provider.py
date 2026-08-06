from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Abstract LLM provider.
    """

    @abstractmethod
    async def chat(self, prompt: str) -> str:
        """
        Generate a response.
        """
        raise NotImplementedError