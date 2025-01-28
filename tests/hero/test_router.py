import pytest
from sqlalchemy import select
from sqlalchemy.sql.functions import count

from src.hero.models import Hero


@pytest.mark.asyncio
async def test_create_hero(client, db, session):
    response = await client.post("/hero", json={"name": "DogPool"})

    assert response.status_code == 200
    assert response.json().get("name") == "DogPool"
    assert response.json().get("id") == 1

    hero_count = await session.scalars(select(count(Hero.name)).where(Hero.name == "DogPool"))
    assert hero_count.one() == 1


@pytest.mark.asyncio
async def test_get_hero(client, db, session):
    names = ["Ugandan Knuckles", "Spooder Man"]
    heroes = [Hero(name=name) for name in names]
    session.add_all(heroes)
    await session.commit()
