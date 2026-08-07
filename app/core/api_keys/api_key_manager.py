from __future__ import annotations

import secrets


class APIKeyManager:
    """
    Production-ready API key manager.

    This implementation provides API key generation and validation.
    It can later be extended to use Redis or a database.
    """

    def __init__(self) -> None:
        self._keys: set[str] = set()

    def generate(self) -> str:
        """
        Generate and register a new API key.
        """

        key = secrets.token_urlsafe(32)

        self._keys.add(key)

        return key

    def register(
        self,
        key: str,
    ) -> None:
        """
        Register an existing API key.
        """

        self._keys.add(key)

    def validate(
        self,
        key: str,
    ) -> bool:
        """
        Validate an API key.
        """

        return key in self._keys

    def revoke(
        self,
        key: str,
    ) -> None:
        """
        Revoke an API key.
        """

        self._keys.discard(key)
