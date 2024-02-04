import uvicorn

from fastapi import FastAPI

from backend.src.routers import users_router
from backend.src.routers import devices_router
from backend.src.utils.config import config

app = FastAPI()

app.include_router(users_router, prefix="/api")
app.include_router(devices_router, prefix="/api")


def run_server():
    uvicorn.run("main:app", reload=True, host=config.IP, port=config.PORT)


if __name__ == "__main__":
    run_server()