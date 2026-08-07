from __future__ import annotations

import secrets


class JWTManager:
    """
    Lightweight JWT manager.

    This class provides a simple authentication token interface.
    It can later be replaced with a real JWT implementation.
    """

    def create_token(
        self,
        subject: str,
    ) -> str:
        """
        Create a token for a subject.
        """

        return f"{subject}:{secrets.token_hex(16)}"

    def verify_token(
        self,
        token: str,
    ) -> bool:
        """
        Verify a token.
        """

        return ":" in token and len(token.split(":", maxsplit=1)[1]) > 0
