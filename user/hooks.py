from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.db import create_db_tables, close_db_conn


@asynccontextmanager
async def initialize_db(app: FastAPI):
    # Startup
    await create_db_tables()

    yield

    # Shutdown
    await close_db_conn()
