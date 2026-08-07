from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from app.application.commands.chat_command import ChatCommand
from app.application.pipeline.chat_pipeline import ChatPipeline
from app.domain.entities.chat_result import ChatResult


class FailoverSelector:
    """
    Returns Groq first, then Gemini.
    """

    def __init__(
        self,
        groq: AsyncMock,
        gemini: AsyncMock,
    ) -> None:
        self._providers = [
            groq,
            gemini,
        ]
        self._index = 0

    def select(self) -> AsyncMock:
        provider = self._providers[self._index]

        if self._index < len(self._providers) - 1:
            self._index += 1

        return provider


@pytest.mark.asyncio
async def test_runtime_failover_to_gemini() -> None:
    groq = AsyncMock()
    gemini = AsyncMock()

    groq.chat.side_effect = RuntimeError("Groq unavailable")

    gemini.chat.return_value = ChatResult(
        response="Response from Gemini",
        provider="gemini",
        model="gemini-2.5-pro",
    )

    selector = FailoverSelector(
        groq=groq,
        gemini=gemini,
    )

    pipeline = ChatPipeline(
        provider_selector=selector,
    )

    result = await pipeline.execute(
        ChatCommand(
            prompt="Hello",
            provider="groq",
            model="llama-3.3-70b-versatile",
        ),
    )

    assert result.provider == "gemini"
    assert result.response == "Response from Gemini"

    assert groq.chat.await_count == 1
    assert gemini.chat.await_count == 1
