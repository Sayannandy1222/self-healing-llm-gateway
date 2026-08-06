from app.domain.providers.provider import LLMProvider


class ChatService:
    """
    Chat application service.
    """

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self.provider = provider

    async def chat(
        self,
        prompt: str,
    ) -> str:
        return await self.provider.chat(prompt)