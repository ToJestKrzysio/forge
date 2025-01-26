from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings

class EnvironmentEnum(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"

    def docs_available(self):
        show_docs_environments = {EnvironmentEnum.DEVELOPMENT}
        return self in show_docs_environments

class GlobalSettings(BaseSettings):
    environment: EnvironmentEnum = Field(validation_alias="ENVIRONMENT", default=EnvironmentEnum.DEVELOPMENT)

