from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str


class IntegrationDBConfig(DBConfig):
    DB_HOST: str = "localhost"
    DB_PORT: str = "27017"
    DB_USERNAME: str = "sentinel_db"
    DB_PASSWORD: str = "Aa123456"
    DB_NAME: str = "integration-sentinel"


class ProductionDBConfig(DBConfig):
    DB_HOST: str = "production-db"
    DB_PORT: str = "27017"
    DB_USERNAME: str = "prod_user"
    DB_PASSWORD: str = "prod_password"
    DB_NAME: str = "production-sentinel"
