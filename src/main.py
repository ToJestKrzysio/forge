from fastapi import FastAPI

from src.common.config import GlobalSettings

from src.health.router import router as health_router

app_config = {"title": "My awesome app"}
if not GlobalSettings().environment.docs_available():
    app_config["openapi_url"] = None  # set url for docs as null

app = FastAPI(**app_config)
app.include_router(health_router)
