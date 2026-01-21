"""Tests for health check endpoint."""

from fastapi.testclient import TestClient


class TestHealthEndpoint:
    """Tests for the /health endpoint."""

    def test_health_returns_200(self, client: TestClient) -> None:
        """Health endpoint should return 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_ok_status(self, client: TestClient) -> None:
        """Health endpoint should return JSON with status 'ok'."""
        response = client.get("/health")
        data = response.json()
        assert data == {"status": "ok"}
