from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings

from src.common.utils.validate_subclasses_mixin import ValidateSubclassesMixin


class EnvironmentEnum(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"

    def docs_available(self):
        show_docs_environments = {EnvironmentEnum.DEVELOPMENT}
        return self in show_docs_environments


class GlobalSettings(BaseSettings, ValidateSubclassesMixin):
    environment: EnvironmentEnum = Field(validation_alias="ENVIRONMENT", default=EnvironmentEnum.DEVELOPMENT)
    debug: bool = Field(validation_alias="DEBUG", default=False)


class PostgresSettings(BaseSettings, ValidateSubclassesMixin):
    host: str = Field(validation_alias="POSTGRES_HOST")
    port: int = Field(validation_alias="POSTGRES_PORT")
    user: str = Field(validation_alias="POSTGRES_USER")
    password: str = Field(validation_alias="POSTGRES_PASSWORD")
    database: str = Field(validation_alias="POSTGRES_DB")

    @property
    def connection_string(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
