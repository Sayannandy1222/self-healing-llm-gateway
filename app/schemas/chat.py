from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Chat completion request.
    """

    prompt: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Prompt submitted by the client.",
    )


class ChatResponse(BaseModel):
    """
    Chat completion response.
    """

    id: str = Field(default_factory=lambda: f"chat_{uuid4().hex}")

    response: str

    provider: str

    model: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
