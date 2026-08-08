from __future__ import annotations

import time

from google import genai

from app.core.settings import settings
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider
from app.infrastructure.observability.prometheus import (
    PROVIDER_FAILURE_COUNTER,
    PROVIDER_LATENCY,
    PROVIDER_REQUEST_COUNTER,
)


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
        start_time = time.perf_counter()

        PROVIDER_REQUEST_COUNTER.labels(provider="gemini").inc()

        try:
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

        except Exception:
            PROVIDER_FAILURE_COUNTER.labels(provider="gemini").inc()
            raise

        finally:
            PROVIDER_LATENCY.labels(provider="gemini").observe(
                time.perf_counter() - start_time
            )
