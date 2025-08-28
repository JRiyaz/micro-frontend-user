from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.db import AuthStorage, Database


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    database = Database()
    auth_storage = AuthStorage()
    await database.setup_db()
    await auth_storage.setup_db()

    # Attach database and auth_storage to app object
    app.state.db = database
    app.state.auth_db = auth_storage

    yield

    # Shutdown
    del app.state.db
    del app.state.auth_db
    await database.close()
    await auth_storage.close()
