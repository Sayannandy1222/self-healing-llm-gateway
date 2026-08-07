from __future__ import annotations

from unittest.mock import AsyncMock

from app.application.commands.chat_command import ChatCommand
from app.application.pipeline.chat_pipeline import ChatPipeline
from app.domain.entities.chat_result import ChatResult


class FakeSelector:
    """
    Fake provider selector used for testing.
    """

    def __init__(self, provider: AsyncMock) -> None:
        self._provider = provider

    def select(self) -> AsyncMock:
        return self._provider


async def test_chat_pipeline_uses_selected_provider() -> None:
    provider = AsyncMock()

    provider.chat.return_value = ChatResult(
        response="Hello from provider",
        provider="groq",
        model="llama-3.3-70b-versatile",
    )

    selector = FakeSelector(provider)

    pipeline = ChatPipeline(
        provider_selector=selector,
    )

    result = await pipeline.execute(
        ChatCommand(
            prompt="Hello",
            model="llama-3.3-70b-versatile",
            provider="groq",
        ),
    )

    assert result.response == "Hello from provider"
    assert result.provider == "groq"
    assert result.model == "llama-3.3-70b-versatile"

    provider.chat.assert_awaited_once_with(
        prompt="Hello",
    )
