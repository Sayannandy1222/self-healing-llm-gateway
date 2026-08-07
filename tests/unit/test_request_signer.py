from __future__ import annotations

from app.core.request_signing.request_signer import (
    RequestSigner,
)


def test_sign_and_verify() -> None:
    signer = RequestSigner(
        secret="secret",
    )

    signature = signer.sign(
        "hello",
    )

    assert signer.verify(
        "hello",
        signature,
    )


def test_invalid_signature() -> None:
    signer = RequestSigner(
        secret="secret",
    )

    assert (
        signer.verify(
            "hello",
            "invalid",
        )
        is False
    )
