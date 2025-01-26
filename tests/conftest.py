from typing import AsyncGenerator

import pytest_asyncio
from async_asgi_testclient import TestClient
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", 9000

    async with AsyncClient(transport=ASGITransport(app=app, client=(host, port)), base_url="http://test") as client:
        yield client
