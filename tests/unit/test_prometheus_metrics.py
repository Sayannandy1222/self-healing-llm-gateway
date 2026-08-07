from prometheus_client import generate_latest

from app.infrastructure.observability.prometheus import REQUEST_COUNTER


def test_prometheus_metrics_registered() -> None:
    REQUEST_COUNTER.inc()

    metrics = generate_latest().decode()

    assert "gateway_requests_total" in metrics
