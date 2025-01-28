from typing import AsyncGenerator

import pytest
import pytest_asyncio
from _pytest.monkeypatch import MonkeyPatch
from async_asgi_testclient import TestClient
from httpx import AsyncClient, ASGITransport

from src.common.database import get_engine, Base, get_session
from src.main import app


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", 9000

    async with AsyncClient(transport=ASGITransport(app=app, client=(host, port)), base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session")
def monkeypatch_session():
    m = MonkeyPatch()
    yield m
    m.undo()


@pytest.fixture(autouse=True, scope="session")
def remove_postgres_db_connection_data(monkeypatch_session):
    monkeypatch_session.delenv("POSTGRES_HOST", raising=False)
    monkeypatch_session.delenv("POSTGRES_PORT", raising=False)
    monkeypatch_session.delenv("POSTGRES_USER", raising=False)
    monkeypatch_session.delenv("POSTGRES_PASSWORD", raising=False)
    monkeypatch_session.delenv("POSTGRES_DATABASE", raising=False)


@pytest.fixture(scope="session")
def engine(monkeypatch_session):
    monkeypatch_session.setenv("POSTGRES_HOST", "localhost")
    monkeypatch_session.setenv("POSTGRES_PORT", "5432")
    monkeypatch_session.setenv("POSTGRES_USER", "postgres")
    monkeypatch_session.setenv("POSTGRES_PASSWORD", "Testpass123")
    monkeypatch_session.setenv("POSTGRES_DATABASE", "test")
    return get_engine()


@pytest_asyncio.fixture(scope="function")
async def session(monkeypatch_session, engine):
    await engine.dispose()
    async for session in get_session():
        yield session


@pytest.fixture(scope="function")
def db(engine, event_loop):
    async def create_all():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    async def drop_all():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    event_loop.run_until_complete(create_all())
    yield
    event_loop.run_until_complete(drop_all())
    event_loop.run_until_complete(engine.dispose())
