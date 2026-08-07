from __future__ import annotations

from prometheus_client import Counter, Histogram

REQUEST_COUNTER = Counter(
    "gateway_requests_total",
    "Total number of chat requests.",
)

PROVIDER_REQUEST_COUNTER = Counter(
    "provider_requests_total",
    "Total requests handled by each provider.",
    ["provider"],
)

PROVIDER_FAILURE_COUNTER = Counter(
    "provider_failures_total",
    "Total provider failures.",
    ["provider"],
)

PROVIDER_LATENCY = Histogram(
    "provider_latency_seconds",
    "Provider request latency.",
    ["provider"],
)
