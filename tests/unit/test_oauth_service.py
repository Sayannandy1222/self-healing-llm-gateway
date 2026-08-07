from datetime import UTC

from app.core.oauth.oauth_service import OAuthService


def test_issue_access_token() -> None:
    service = OAuthService()

    token = service.issue_access_token(
        "alice",
    )

    assert token.startswith("alice:")


def test_issue_refresh_token() -> None:
    service = OAuthService()

    token = service.issue_refresh_token(
        "alice",
    )

    assert "refresh" in token


def test_expiration_is_timezone_aware() -> None:
    service = OAuthService()

    expires = service.expires_at()

    assert expires.tzinfo == UTC
