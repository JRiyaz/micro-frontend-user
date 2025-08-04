from fastapi import FastAPI

from .routes.user import user_routes


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        version="1.0.0",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1, "deepLinking": False},
    )

    app.include_router(user_routes)

    return app
