from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from src.common.config import PostgresSettings, GlobalSettings


class Base(DeclarativeBase):
    pass


def get_engine():
    ps = PostgresSettings()
    global_settings = GlobalSettings()
    connection_string = f"postgresql://{ps.user}:{ps.password}@{ps.host}:{ps.port}/{ps.database}"
    return create_engine(connection_string, echo=global_settings.debug)
