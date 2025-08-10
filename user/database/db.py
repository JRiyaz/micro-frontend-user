import logging
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
)
from sqlalchemy.ext.asyncio import (
    async_sessionmaker as session_maker,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine as create_engine,
)
from sqlmodel import Session

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
        self.pool_size: int = config.DB_POOL_SIZE
        self.max_overflow: int = config.DB_MAX_OVERFLOW
        self.pool_timeout: int = config.DB_POOL_TIMEOUT
        self.pool_recycle: int = config.DB_POOL_RECYCLE
        self.db: str = config.DB.get_db_str()
        self.db_logs: bool = config.DB_LOGS

        self.conn_str: str = f"{self.db}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine: AsyncEngine = create_engine(
            self.conn_str,
            echo=self.db_logs,
            pool_size=self.pool_size,  # Max number of connections
            max_overflow=self.max_overflow,  # Extra connections if pool is full
            pool_timeout=self.pool_timeout,  # Seconds to wait before giving up on getting a connection
            pool_recycle=self.pool_recycle,  # Recycle connections after 30 minutes)
        )
        self.async_session: session_maker = session_maker(self.engine, class_=AsyncSession, expire_on_commit=False)

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    # def db_session(self):
    #     with Session(self.engine) as session:
    #         yield session


db: Database = Database()


async def create_db_tables() -> None:
    logger.error("Creating database tables")
    await db.create_tables()


async def close_db_conn() -> None:
    logger.error("Closing database connection")
    await db.engine.dispose()


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with db.async_session() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
