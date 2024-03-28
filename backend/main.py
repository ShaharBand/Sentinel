import uvicorn

from fastapi import FastAPI

from src.config.manager import ConfigManager
from src.middleware.db import init_db
from src.routers import *

app = FastAPI(root_path="/api")


@app.on_event("startup")
async def startup_event():
    await init_db()


app.include_router(users_router)
app.include_router(devices_router)


def run_server():
    app_config = ConfigManager.get_app_config()
    uvicorn.run("main:app", reload=True, host=app_config.IP, port=app_config.PORT)


if __name__ == "__main__":
    run_server()
