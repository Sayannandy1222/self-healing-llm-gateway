from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.routers.auth import router

app = FastAPI()

app.include_router(router)

client = TestClient(app)


def test_login_returns_tokens() -> None:
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "alice",
            "password": "secret",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["token_type"] == "bearer"

    assert "access_token" in body

    assert "refresh_token" in body
