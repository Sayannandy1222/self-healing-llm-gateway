from pathlib import Path


def test_ci_workflow_exists() -> None:
    assert Path(".github/workflows/ci.yml").exists()


def test_ci_contains_python() -> None:
    workflow = Path(
        ".github/workflows/ci.yml",
    ).read_text()

    assert "setup-python" in workflow


def test_ci_runs_pytest() -> None:
    workflow = Path(
        ".github/workflows/ci.yml",
    ).read_text()

    assert "pytest" in workflow


def test_ci_runs_mypy() -> None:
    workflow = Path(
        ".github/workflows/ci.yml",
    ).read_text()

    assert "mypy" in workflow


def test_ci_runs_black() -> None:
    workflow = Path(
        ".github/workflows/ci.yml",
    ).read_text()

    assert "black" in workflow


def test_ci_runs_ruff() -> None:
    workflow = Path(
        ".github/workflows/ci.yml",
    ).read_text()

    assert "ruff" in workflow
