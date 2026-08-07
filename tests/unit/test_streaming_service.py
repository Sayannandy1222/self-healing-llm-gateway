from __future__ import annotations

import pytest

from app.application.streaming.streaming_service import (
    StreamingService,
)


@pytest.mark.asyncio
async def test_streaming_service_streams_tokens() -> None:
    service = StreamingService()

    tokens: list[str] = []

    async for token in service.stream(
        "Hello world from gateway",
    ):
        tokens.append(token)

    assert tokens == [
        "Hello ",
        "world ",
        "from ",
        "gateway ",
    ]


@pytest.mark.asyncio
async def test_empty_response() -> None:
    service = StreamingService()

    tokens: list[str] = []

    async for token in service.stream(""):
        tokens.append(token)

    assert tokens == []
