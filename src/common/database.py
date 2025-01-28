from asyncio import current_task

from fastapi import Depends
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated, AsyncGenerator

from src.common.config import PostgresSettings, GlobalSettings


class Base(DeclarativeBase):
    pass


def get_engine():
    postgres_settings = PostgresSettings()
    global_settings = GlobalSettings()
    return create_async_engine(
        postgres_settings.connection_string,
        echo=global_settings.debug,
        # To fix problem with unittests failing due to "sqlalchemy.dialects.postgresql.asyncpg.InterfaceError -
        # cannot perform operation: another operation is in progress" engine.dispose() has to be called before
        # handing control over to another thread or # poolclass=NullPool has to be specified for engine
        # Currently no crushing advantage found for any of these
    )


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    engine = get_engine()
    session_maker = async_scoped_session(
        async_sessionmaker(autocommit=False, bind=engine, expire_on_commit=False),
        scopefunc=current_task,
    )
    async with session_maker() as session:
        yield session
        await session.close()


SessionDependency = Annotated[AsyncSession, Depends(get_session)]


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
