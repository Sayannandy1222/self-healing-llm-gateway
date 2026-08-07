from pathlib import Path


def test_deployment_exists() -> None:
    assert Path("k8s/deployment.yaml").exists()


def test_service_exists() -> None:
    assert Path("k8s/service.yaml").exists()


def test_configmap_exists() -> None:
    assert Path("k8s/configmap.yaml").exists()


def test_secret_exists() -> None:
    assert Path("k8s/secret.yaml").exists()


def test_ingress_exists() -> None:
    assert Path("k8s/ingress.yaml").exists()


def test_hpa_exists() -> None:
    assert Path("k8s/hpa.yaml").exists()
