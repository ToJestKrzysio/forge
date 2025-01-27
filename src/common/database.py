from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase

from src.common.config import PostgresSettings, GlobalSettings


class Base(DeclarativeBase):
    pass


def get_engine():
    postgres_settings = PostgresSettings()
    global_settings = GlobalSettings()
    return create_engine(postgres_settings.connection_string, echo=global_settings.debug)


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
