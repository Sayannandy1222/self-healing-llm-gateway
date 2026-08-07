from __future__ import annotations

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security.jwt import JWTManager

security = HTTPBearer()

jwt_manager = JWTManager()


def require_auth(
    credentials: HTTPAuthorizationCredentials = Security(
        security,
    ),
) -> str:
    """
    Require a valid authentication token.
    """

    token = credentials.credentials

    if not jwt_manager.verify_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token.",
        )

    return token
