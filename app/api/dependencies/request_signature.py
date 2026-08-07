from __future__ import annotations

from fastapi import Header, HTTPException, status

from app.core.request_signing.request_signer import RequestSigner

_signer = RequestSigner(
    secret="development-secret",
)


def require_request_signature(
    message: str,
    x_signature: str = Header(
        alias="X-Signature",
    ),
) -> None:
    """
    Verify an incoming request signature.
    """

    if not _signer.verify(
        message,
        x_signature,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid request signature.",
        )
