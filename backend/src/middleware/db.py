from beanie import init_beanie
import motor.motor_asyncio

from src.config.manager import ConfigManager
from src.dal.entities.user import User
from src.dal.entities.device import Device


async def init_db():
    db_config = ConfigManager.get_db_config()
    db_uri = f'mongodb://{db_config.DB_USERNAME}:{db_config.DB_PASSWORD}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}'

    client = motor.motor_asyncio.AsyncIOMotorClient(
        db_uri
    )

    await init_beanie(database=client.db_name, document_models=[Device, User])
