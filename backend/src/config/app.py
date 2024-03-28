from pydantic_settings import BaseSettings

from src.config.environment import Environment


class AppConfig(BaseSettings):
    IP: str = "127.0.0.1"
    PORT: int = 5000
    ENVIRONMENT: Environment = Environment.integration
