from enum import Enum

from pydantic.v1 import BaseSettings


class Databases(Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"

    def get_db_str(self) -> str:
        if self.value == "postgres":
            return "postgresql+psycopg2"
        else:
            return "mysql"


class Config(BaseSettings):
    # Environment Configuration
    ENV: str = "development"

    # Database Configuration
    DB: Databases
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_LOGS: bool = False


config = Config()
