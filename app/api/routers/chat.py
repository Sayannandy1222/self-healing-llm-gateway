from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import StreamingResponse

from app.api.dependencies.auth import require_auth
from app.api.dependencies.chat import get_chat_service
from app.application.services.chat_service import ChatService
from app.application.streaming.streaming_service import StreamingService
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate AI response",
)
async def chat(
    request: ChatRequest,
    _: Annotated[
        str,
        Depends(require_auth),
    ],
    service: Annotated[
        ChatService,
        Depends(get_chat_service),
    ],
) -> ChatResponse:
    """
    Generate a complete AI response.
    """

    result = await service.generate(
        request.prompt,
    )

    return ChatResponse(
        response=result.response,
        provider=result.provider,
        model=result.model,
    )


@router.post(
    "/chat/stream",
    status_code=status.HTTP_200_OK,
    summary="Stream AI response",
)
async def stream_chat(
    request: ChatRequest,
    _: Annotated[
        str,
        Depends(require_auth),
    ],
    service: Annotated[
        ChatService,
        Depends(get_chat_service),
    ],
) -> StreamingResponse:
    """
    Stream an AI response token by token.
    """

    result = await service.generate(
        request.prompt,
    )

    streaming_service = StreamingService()

    return StreamingResponse(
        streaming_service.stream(
            result.response,
        ),
        media_type="text/event-stream",
    )
