from fastapi import Depends
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated

from src.common.config import PostgresSettings, GlobalSettings


class Base(DeclarativeBase):
    pass


def get_engine():
    postgres_settings = PostgresSettings()
    global_settings = GlobalSettings()
    return create_async_engine(postgres_settings.connection_string, echo=global_settings.debug)


async def get_session():
    engine = get_engine()
    session_maker = async_sessionmaker(autocommit=False, bind=engine, expire_on_commit=False)
    async with session_maker() as session:
        yield session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
