import pytest
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_health(client: TestClient) -> None:
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
