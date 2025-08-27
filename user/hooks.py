from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.db import auth_storage, database


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    await database.setup_db()
    await auth_storage.setup_db()
    app.state.db = database
    app.state.auth_db = auth_storage.storage

    yield

    # Shutdown
    del app.state.auth_db
    del app.state.db
    await database.close()
    await auth_storage.close()
