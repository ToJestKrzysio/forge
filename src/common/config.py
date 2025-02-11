from enum import Enum
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings

from src.common.utils.validate_subclasses_mixin import ValidateSubclassesMixin


class EnvironmentEnum(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"

    def docs_available(self):
        show_docs_environments = {EnvironmentEnum.DEVELOPMENT}
        return self in show_docs_environments


ALLOWED_METHODS = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "*"]


def get_default_allowed_methods() -> list[ALLOWED_METHODS]:
    return ["GET"]


class GlobalSettings(BaseSettings, ValidateSubclassesMixin):
    environment: EnvironmentEnum = Field(validation_alias="ENVIRONMENT", default=EnvironmentEnum.DEVELOPMENT)
    debug: bool = Field(validation_alias="DEBUG", default=False)
    cors_allow_origins: list[str] = Field(  # noqa: pycharm false positive for default_factory
        validation_alias="CORS_ALLOW_ORIGINS", default_factory=lambda values: ["*"] if values["debug"] is True else []
    )
    cors_allow_credentials: bool = Field(validation_alias="CORS_ALLOW_CREDENTIALS", default=False)
    cors_allow_methods: list[ALLOWED_METHODS] = Field(  # noqa: pycharm false positive for default_factory
        validation_alias="CORS_ALLOW_METHODS", default_factory=lambda: ["GET"]
    )
    cors_allow_headers: list[str] = Field(  # noqa: pycharm false positive for default_factory
        validation_alias="CORS_ALLOW_HEADERS", default_factory=lambda: ["Authorization", "Content-Type"]
    )


class PostgresSettings(BaseSettings, ValidateSubclassesMixin):
    host: str = Field(validation_alias="POSTGRES_HOST")
    port: int = Field(validation_alias="POSTGRES_PORT")
    user: str = Field(validation_alias="POSTGRES_USER")
    password: str = Field(validation_alias="POSTGRES_PASSWORD")
    database: str = Field(validation_alias="POSTGRES_DB")

    @property
    def connection_string(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
