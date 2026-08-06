from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider


class ChatService:
    """
    Coordinates chat interactions.
    """

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self.provider = provider

    async def generate(
        self,
        prompt: str,
    ) -> ChatResult:
        """
        Generate a chat completion.
        """

        return await self.provider.chat(prompt)
