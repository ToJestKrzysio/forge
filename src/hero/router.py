from fastapi import APIRouter
from sqlalchemy import select

from src.common.database import SessionDependency
from src.hero.models import Hero
from src.hero.schema import CreateHeroSchema, GetHeroSchema, ListHeroSchema

router = APIRouter(prefix="/hero", tags=["hero"])


@router.post("", response_model=GetHeroSchema)
async def create_hero(hero: CreateHeroSchema, session: SessionDependency):
    db_hero = Hero(**hero.model_dump())
    session.add(db_hero)
    await session.commit()

    await session.refresh(db_hero)
    return GetHeroSchema.model_validate(db_hero)


@router.get("", response_model=ListHeroSchema)
async def get_heroes(session: SessionDependency):
    query = select(Hero).order_by(Hero.id).limit(10)
    result = await session.scalars(query)

    return ListHeroSchema.model_validate(result.all())
