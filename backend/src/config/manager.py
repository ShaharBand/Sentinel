from functools import lru_cache

from src.config.app import AppConfig
from src.config.db import IntegrationDBConfig, ProductionDBConfig, DBConfig
from src.config.environment import Environment

ENVIRONMENT_TO_DB_CONFIG = {
    Environment.integration: IntegrationDBConfig(),
    Environment.production: ProductionDBConfig(),
}


class ConfigManager:
    @classmethod
    @lru_cache(maxsize=1)
    def get_app_config(cls) -> AppConfig:
        return AppConfig()

    @classmethod
    @lru_cache(maxsize=1)
    def get_db_config(cls) -> DBConfig:
        return ENVIRONMENT_TO_DB_CONFIG.get(cls.get_app_config().ENVIRONMENT)
