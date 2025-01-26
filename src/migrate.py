from src.common.database import get_engine, Base

from src.sample.models import Hero  # noqa


def main():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)


main()
