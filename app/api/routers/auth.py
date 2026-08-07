from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.oauth.oauth_service import OAuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


_service = OAuthService()


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    request: LoginRequest,
) -> TokenResponse:
    """
    Authenticate a user and return tokens.
    """

    # Placeholder authentication.
    # Replace later with a real user store.
    access = _service.issue_access_token(
        request.username,
    )

    refresh = _service.issue_refresh_token(
        request.username,
    )

    return TokenResponse(
        access_token=access,
        refresh_token=refresh,
        token_type="bearer",
    )
