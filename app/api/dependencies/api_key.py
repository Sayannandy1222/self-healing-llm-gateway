from __future__ import annotations

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.core.api_keys.api_key_manager import APIKeyManager

api_key_header = APIKeyHeader(
    name="X-API-Key",
)

api_key_manager = APIKeyManager()


def require_api_key(
    api_key: str = Security(
        api_key_header,
    ),
) -> str:
    """
    Validate an API key.
    """

    if not api_key_manager.validate(api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )

    return api_key
