from asyncio import get_event_loop

from src.common.database import get_engine, Base

from src.hero.models import Hero  # noqa


async def migrate():
    engine = get_engine()
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


def main():
    loop = get_event_loop()
    loop.run_until_complete(migrate())


if __name__ == "__main__":
    main()
