from __future__ import annotations

import os
from collections.abc import Iterator
from contextlib import contextmanager

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

SERVICE_NAME = "self-healing-llm-gateway"


def configure_tracing() -> None:
    """Configure OpenTelemetry tracing for the gateway."""

    endpoint = os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT",
        "http://localhost:4317",
    )

    resource = Resource.create(
        {
            "service.name": SERVICE_NAME,
            "service.version": "0.1.0",
            "deployment.environment": os.getenv(
                "ENVIRONMENT",
                "development",
            ),
        }
    )

    provider = TracerProvider(resource=resource)

    exporter = OTLPSpanExporter(
        endpoint=endpoint,
        insecure=True,
    )

    provider.add_span_processor(BatchSpanProcessor(exporter))

    trace.set_tracer_provider(provider)


class Tracer:
    """Application tracing abstraction backed by OpenTelemetry."""

    def __init__(self) -> None:
        self._tracer = trace.get_tracer("self-healing-llm-gateway")

    @contextmanager
    def start_span(
        self,
        name: str,
    ) -> Iterator[None]:
        """Start an OpenTelemetry span."""

        with self._tracer.start_as_current_span(name):
            yield
