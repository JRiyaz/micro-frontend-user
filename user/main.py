from typing import Union
from fastapi import FastAPI


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        version="1.0.0",
    )

    @app.get("/")
    def read_root():
        return {"version": app.version}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    # Include routers, middleware, etc.
    # from .routers import user_router
    # app.include_router(user_router)

    return app
