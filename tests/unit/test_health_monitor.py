from app.infrastructure.telemetry.health_monitor import HealthMonitor


def test_register_provider() -> None:
    monitor = HealthMonitor()

    monitor.register("groq")

    assert monitor.is_healthy("groq")


def test_mark_unhealthy() -> None:
    monitor = HealthMonitor()

    monitor.register("groq")

    monitor.mark_unhealthy("groq")

    assert monitor.is_healthy("groq") is False

    assert monitor.get("groq").failure_count == 1


def test_mark_healthy() -> None:
    monitor = HealthMonitor()

    monitor.register("groq")

    monitor.mark_unhealthy("groq")

    monitor.mark_healthy(
        "groq",
        latency_ms=125,
    )

    assert monitor.is_healthy("groq")

    assert monitor.get("groq").failure_count == 0

    assert monitor.get("groq").latency_ms == 125
