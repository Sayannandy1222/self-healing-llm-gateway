from __future__ import annotations

from app.infrastructure.tracing.tracer import Tracer


def test_start_span() -> None:
    tracer = Tracer()

    with tracer.start_span("chat"):
        value = 42

    assert value == 42


def test_nested_spans() -> None:
    tracer = Tracer()

    with tracer.start_span("outer"):
        with tracer.start_span("inner"):
            value = "ok"

    assert value == "ok"
