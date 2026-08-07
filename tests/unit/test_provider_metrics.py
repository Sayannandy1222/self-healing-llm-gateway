from app.infrastructure.metrics.provider_metrics import ProviderMetrics


def test_provider_metrics_defaults() -> None:
    metrics = ProviderMetrics(
        provider="groq",
    )

    assert metrics.provider == "groq"
    assert metrics.total_requests == 0
    assert metrics.successful_requests == 0
    assert metrics.failed_requests == 0
    assert metrics.average_latency_ms == 0.0
    assert metrics.success_rate == 0.0


def test_average_latency() -> None:
    metrics = ProviderMetrics(
        provider="groq",
        total_requests=2,
        total_latency_ms=300,
    )

    assert metrics.average_latency_ms == 150.0


def test_success_rate() -> None:
    metrics = ProviderMetrics(
        provider="groq",
        total_requests=10,
        successful_requests=8,
    )

    assert metrics.success_rate == 0.8
