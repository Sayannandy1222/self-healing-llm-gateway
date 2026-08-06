from app.infrastructure.telemetry.provider_health import ProviderHealth


def test_provider_health_defaults() -> None:
    health = ProviderHealth(provider="groq")

    assert health.provider == "groq"
    assert health.healthy is True
    assert health.failure_count == 0
