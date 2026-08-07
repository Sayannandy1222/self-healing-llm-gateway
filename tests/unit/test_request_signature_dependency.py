from __future__ import annotations

import pytest
from fastapi import HTTPException

from app.api.dependencies.request_signature import (
    require_request_signature,
)
from app.core.request_signing.request_signer import (
    RequestSigner,
)


def test_valid_signature() -> None:
    signer = RequestSigner(
        secret="development-secret",
    )

    signature = signer.sign(
        "hello",
    )

    require_request_signature(
        message="hello",
        x_signature=signature,
    )


def test_invalid_signature() -> None:
    with pytest.raises(HTTPException):
        require_request_signature(
            message="hello",
            x_signature="invalid",
        )
