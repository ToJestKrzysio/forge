from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import ValidationError

from src.common.config import GlobalSettings
from src.common.utils.validate_subclasses_mixin import ValidateSubclassesMixin

from src.health.router import router as health_router

app_config = {"title": "My awesome app"}
if not GlobalSettings().environment.docs_available():
    app_config["openapi_url"] = None  # set url for docs as null


@asynccontextmanager
async def lifespan(_app: FastAPI):
    ValidateSubclassesMixin.validate_subclasses()
    yield


app = FastAPI(**app_config, lifespan=lifespan)
app.include_router(health_router)
