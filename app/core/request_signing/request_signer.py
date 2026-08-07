from __future__ import annotations

import hashlib
import hmac


class RequestSigner:
    """
    HMAC-SHA256 request signer.
    """

    def __init__(
        self,
        secret: str,
    ) -> None:
        self._secret = secret.encode()

    def sign(
        self,
        message: str,
    ) -> str:
        """
        Generate a request signature.
        """

        return hmac.new(
            self._secret,
            message.encode(),
            hashlib.sha256,
        ).hexdigest()

    def verify(
        self,
        message: str,
        signature: str,
    ) -> bool:
        """
        Verify a request signature.
        """

        expected = self.sign(message)

        return hmac.compare_digest(
            expected,
            signature,
        )
