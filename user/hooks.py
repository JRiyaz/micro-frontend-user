from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.db import Database, AuthStorage


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    database = Database(app)
    auth_storage = AuthStorage()
    await database.setup_db(auth_storage)
    await auth_storage.setup_db()

    yield

    # Shutdown
    await database.close()
    await auth_storage.close()
