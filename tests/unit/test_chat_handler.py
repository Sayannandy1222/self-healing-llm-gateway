from unittest.mock import AsyncMock

import pytest

from app.application.commands.chat_command import ChatCommand
from app.application.handlers.chat_handler import ChatHandler
from app.domain.entities.chat_result import ChatResult


@pytest.mark.asyncio
async def test_chat_handler_executes_pipeline() -> None:
    pipeline = AsyncMock()

    expected = ChatResult(
        response="hello",
        provider="groq",
        model="llama",
        finish_reason="stop",
    )

    pipeline.execute.return_value = expected

    handler = ChatHandler(pipeline)

    command = ChatCommand(
        prompt="hi",
        provider="groq",
        model="llama",
    )

    result = await handler.execute(command)

    assert result == expected

    pipeline.execute.assert_awaited_once_with(command)
