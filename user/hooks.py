from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.db import close_db_conn, create_db_tables
from .logger import setup_logging


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    setup_logging()
    await create_db_tables()

    yield

    # Shutdown
    await close_db_conn()
