from functools import lru_cache

from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    # Application Configuration
    IP: str = "127.0.0.1"
    PORT: int = 5000
    VERSION: str = "0.0.1"

    # Database Configuration
    DB_USERNAME: str = "sentinel_db"
    DB_PASSWORD: str = "Aa123456"
    DB_HOST: str = "localhost"
    DB_PORT: str = "27017"
    DB_NAME: str = "sentinel"


class AppConfigManager:
    _config = AppConfig()

    @classmethod
    @lru_cache(maxsize=1)
    def get_config(cls) -> AppConfig:
        return cls._config

    @classmethod
    @lru_cache(maxsize=1)
    def get_db_uri(cls) -> str:
        db_config = cls.get_config()
        uri = f'mongodb://{db_config.DB_USERNAME}:{db_config.DB_PASSWORD}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}'
        return uri


db_uri = AppConfigManager().get_db_uri()
config = AppConfigManager().get_config()
