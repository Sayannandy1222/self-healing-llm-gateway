from __future__ import annotations

from datetime import UTC, datetime, timedelta

from app.core.security.jwt import JWTManager


class OAuthService:
    """
    OAuth2 authentication service.
    """

    def __init__(
        self,
        jwt_manager: JWTManager | None = None,
    ) -> None:
        self._jwt = jwt_manager or JWTManager()

    def issue_access_token(
        self,
        username: str,
    ) -> str:
        """
        Issue an access token.
        """

        return self._jwt.create_token(username)

    def issue_refresh_token(
        self,
        username: str,
    ) -> str:
        """
        Issue a refresh token.
        """

        return self._jwt.create_token(
            f"{username}:refresh",
        )

    def expires_at(
        self,
        minutes: int = 30,
    ) -> datetime:
        """
        Compute the expiration time.
        """

        return datetime.now(
            UTC,
        ) + timedelta(
            minutes=minutes,
        )
