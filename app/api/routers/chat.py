from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.chat import get_chat_service
from app.application.services.chat_service import ChatService
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
    service: Annotated[
        ChatService,
        Depends(get_chat_service),
    ],
) -> ChatResponse:
    """
    Generate an AI response.
    """

    result = await service.generate(
        request.prompt,
    )

    return ChatResponse(
        response=result.response,
        provider=result.provider,
        model=result.model,
    )
