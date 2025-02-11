import asyncio
from contextlib import asynccontextmanager

import uvloop
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.admin import admin
from src.common.config import GlobalSettings
from src.common.database import get_engine
from src.common.middlewares import set_security_headers
from src.health.router import router as health_router
from src.hero.router import router as hero_router
from src.liefespan import startup, teardown

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

settings = GlobalSettings()

app_config = {"title": "My awesome app"}
if not settings.environment.docs_available():
    app_config["openapi_url"] = None  # set url for docs as null


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await startup(_app)
    yield
    await teardown(_app)


app = FastAPI(**app_config, lifespan=lifespan)

app.include_router(health_router)
app.include_router(hero_router)  # TODO REMOVE

admin.build(app, get_engine())

app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=settings.cors_allow_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

app.middleware("http")(set_security_headers)  # noqa
