from google import genai

from app.core.settings import settings
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider


class GeminiProvider(LLMProvider):
    """
    Google Gemini implementation of the provider contract.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    async def chat(
        self,
        prompt: str,
    ) -> ChatResult:
        response = self.client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
        )

        return ChatResult(
            response=response.text or "",
            provider="gemini",
            model=settings.gemini_model,
            finish_reason="STOP",
        )
