import logging
from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.engine.base import Engine
from sqlmodel import Session, create_engine

from ..config import config
from ..model import SQLModel

logger = logging.getLogger(__name__)


class Database:
    def __init__(self):
        self.host: str = config.DB_HOST
        self.port: int = config.DB_PORT
        self.user: str = config.DB_USER
        self.password: str = config.DB_PASSWORD
        self.database: str = config.DB_DATABASE
        self.db: str = config.DB.get_db_str()
        self.db_logs: bool = config.DB_LOGS

        self.conn_str: str = f"{self.db}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine: Engine = create_engine(self.conn_str, echo=self.db_logs)

    def create_tables(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    # def db_session(self):
    #     with Session(self.engine) as session:
    #         yield session


db: Database = Database()


def create_db_tables() -> None:
    logger.error("Creating database tables")
    db.create_tables()


def get_db() -> Generator[Session]:
    with Session(db.engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
