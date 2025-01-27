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
    debug: bool = Field(validation_alias="DEBUG", default=True)  # TODO CHANGE AFTER DOCKER


class PostgresSettings(BaseSettings, ValidateSubclassesMixin):
    host: str = Field(validation_alias="POSTGRES_HOST", default="127.0.0.1")  # TODO REMOVE DEFAULT AFTER DOCKER
    port: int = Field(validation_alias="POSTGRES_PORT", default=5432)  # TODO REMOVE DEFAULT AFTER DOCKER
    user: str = Field(validation_alias="POSTGRES_USER", default="postgres")  # TODO REMOVE DEFAULT AFTER DOCKER
    password: str = Field(validation_alias="POSTGRES_PASSWORD", default="Testpass123")  # TODO REMOVE DEFAULT
    database: str = Field(validation_alias="POSTGRES_DATABASE", default="test")

    @property
    def connection_string(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
