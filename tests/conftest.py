from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> Generator[TestClient]:
    """
    Shared FastAPI test client.
    """
    with TestClient(app) as test_client:
        yield test_client
