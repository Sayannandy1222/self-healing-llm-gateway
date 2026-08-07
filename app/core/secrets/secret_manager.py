from __future__ import annotations

import os


class SecretManager:
    """
    Production secret manager.

    Loads secrets from environment variables.
    This abstraction can later be extended to support
    Kubernetes Secrets, Docker Secrets, AWS Secrets Manager,
    Azure Key Vault, or HashiCorp Vault.
    """

    def get(
        self,
        key: str,
        default: str | None = None,
    ) -> str | None:
        """
        Return a secret.
        """

        return os.getenv(
            key,
            default,
        )

    def require(
        self,
        key: str,
    ) -> str:
        """
        Return a required secret.
        """

        value = os.getenv(key)

        if value is None:
            raise RuntimeError(
                f"Missing required secret: {key}",
            )

        return value

    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Check whether a secret exists.
        """

        return key in os.environ
