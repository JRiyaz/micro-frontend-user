from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from .exceptions import validation_handler
from .hooks import initialize_db
from .middlewares import TimeIt
from .routes.common import routes as common_routes
from .routes.user import routes as user_routes


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        docs_url=None,
        lifespan=initialize_db,
    )
    project_path: Path = Path(__file__).parent.parent
    app.project_path = project_path
    app.version = project_path.joinpath(".version").read_text().strip()

    app.add_exception_handler(RequestValidationError, validation_handler)
    app.add_middleware(TimeIt, some_attribute="time")

    app.include_router(common_routes)
    app.include_router(user_routes)

    return app
