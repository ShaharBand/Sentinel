from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.manager import ConfigManager
from src.middleware.db import init_db
from src.routers.users import router as users_router
from src.routers.devices import router as devices_router
from src.routers.statistics import router as statistics_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

config_manager = ConfigManager()
app_metadata = config_manager.get_metadata()
app_config = config_manager.get_app_config()

app = FastAPI(root_path="/api",
              title=app_metadata.NAME,
              description=app_metadata.DESCRIPTION,
              version=app_metadata.VERSION,
              lifespan=lifespan,
              responses={404: {"description": "Not found"}})

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_config.allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(devices_router)
app.include_router(statistics_router)