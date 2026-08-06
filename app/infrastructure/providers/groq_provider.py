from groq import AsyncGroq

from app.core.settings import settings
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider


class GroqProvider(LLMProvider):
    """
    Groq implementation of the provider contract.
    """

    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

    async def chat(
        self,
        prompt: str,
    ) -> ChatResult:

        response = await self.client.chat.completions.create(
            model=settings.default_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        message = response.choices[0].message

        return ChatResult(
            response=message.content or "",
            provider="groq",
            model=response.model,
            finish_reason=response.choices[0].finish_reason,
        )
