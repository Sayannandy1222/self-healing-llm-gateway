from groq import AsyncGroq

from app.core.settings import settings
from app.domain.providers.provider import LLMProvider


class GroqProvider(LLMProvider):
    """
    Groq implementation of the LLM provider.
    """

    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

    async def chat(
        self,
        prompt: str,
    ) -> str:

        response = await self.client.chat.completions.create(
            model=settings.default_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content