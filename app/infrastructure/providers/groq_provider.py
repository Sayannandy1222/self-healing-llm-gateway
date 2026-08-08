from __future__ import annotations

import time

from groq import AsyncGroq

from app.core.settings import settings
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider
from app.infrastructure.observability.prometheus import (
    PROVIDER_FAILURE_COUNTER,
    PROVIDER_LATENCY,
    PROVIDER_REQUEST_COUNTER,
)


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
        start_time = time.perf_counter()

        PROVIDER_REQUEST_COUNTER.labels(provider="groq").inc()

        try:
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

        except Exception:
            PROVIDER_FAILURE_COUNTER.labels(provider="groq").inc()
            raise

        finally:
            PROVIDER_LATENCY.labels(provider="groq").observe(
                time.perf_counter() - start_time
            )
