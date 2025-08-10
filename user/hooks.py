from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db import create_db_tables


@asynccontextmanager
async def initialize_db(app: FastAPI):
    # Startup logic
    create_db_tables()

    yield
