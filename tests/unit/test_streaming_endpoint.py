from __future__ import annotations

from fastapi.responses import StreamingResponse

from app.application.streaming.streaming_service import StreamingService


async def test_streaming_response_creation() -> None:
    service = StreamingService()

    response = StreamingResponse(
        service.stream("Hello world"),
        media_type="text/event-stream",
    )

    assert response.media_type == "text/event-stream"
