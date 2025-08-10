from enum import Enum
from typing import Annotated, Literal

from pydantic import AfterValidator
from pydantic.v1 import BaseSettings

from .utils.string import to_upper


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
    ENV: Literal["development", "production", "testing"] = "development"

    # Log Configuration
    LOG_LEVEL: Annotated[str, AfterValidator(to_upper)] = "ERROR"
    LOG_UVICORN: Annotated[str, AfterValidator(to_upper)] = "INFO"

    # Auth Configuration
    AUTH_COOKIE_NAME: str = "auth_token"

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
