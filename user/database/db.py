import logging
from typing import AsyncGenerator

from fastapi import Request, FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker as session_maker
from sqlalchemy.ext.asyncio import create_async_engine as create_engine

from .redis import RedisStorage
from ..config import config
from ..model import SQLModel

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, app: FastAPI):
        self.app = app
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
        self.engine = None
        self.async_session = None

    async def connect(self):
        logger.info(f"Connecting to database: {config.DB_DATABASE}")
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
        logger.error("Creating database tables")
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def close(self) -> None:
        logger.error("Closing database connection")
        await self.engine.dispose()

    async def get_db(self) -> AsyncGenerator[AsyncSession]:
        async with self.async_session() as session:
            logger.debug(f"********** Getting database session: {session} **********")
            yield session
            logger.debug(f"************ closing database session: {session} **********")

    async def setup_db(self, auth_storage: "AuthStorage") -> None:
        await self.connect()
        await self.create_tables()
        await self.add_session_middleware(auth_storage)

    async def add_session_middleware(self, auth_storage: "AuthStorage"):
        @self.app.middleware("http")
        async def add_db_session(request: Request, call_next):
            # Create session and attach to request
            request.state.db_session = self.async_session()
            request.state.auth_db = auth_storage.storage
            logger.info(f"Attaching DB session: {request.state.db_session}")
            try:
                response = await call_next(request)
            finally:
                print(f"Closing DB session: {request.state.db_session}")
                await request.state.db_session.close()
            return response

    # def db_session(self):
    #     with Session(self.engine) as session:
    #         yield session


# async def get_db(req: Request) -> AsyncGenerator[AsyncSession, None]:
#     async for session in req.app.db.get_async_session():
#         yield session


class AuthStorage:
    def __init__(self):
        self.storage = None

    async def setup_db(self):
        auth_db: str = config.AUTH_DB
        storage = None
        if auth_db == "db":
            logger.info("Initializing db as auth storage")
        elif auth_db == "redis":
            logger.info("Initializing redis as auth storage")
            storage = RedisStorage()
        self.storage = storage

    async def get_db(self):
        return self.storage

    async def close(self):
        if self.storage:
            logger.info("Closing auth storage")
            await self.storage.close()


# DB = Annotated[Session, Depends(database.get_db, use_cache=False)]
# AuthDB = Annotated[Session, Depends(auth_storage.get_db, use_cache=True)]
