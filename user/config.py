from enum import Enum

from pydantic.v1 import BaseSettings


class Databases(Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"

    def get_db_str(self) -> str:
        if self.value == "postgres":
            return "postgresql+asyncpg"
        else:
            return "mysql"


class Config(BaseSettings):
    # Environment Configuration
    ENV: str = "development"

    # Auth Configuration
    AUTH_COOKIE_NAME: str = "access_token"

    # Database Configuration
    DB: Databases
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DB_POOL_TIMEOUT: int
    DB_POOL_RECYCLE: int
    DB_LOGS: bool = False


config = Config()
