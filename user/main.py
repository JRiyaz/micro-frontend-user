import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates

from .exceptions import validation_handler
from .hooks import app_lifespan
from .middlewares import LogIt, TimeIt
from .routes.common import routes as common_routes
from .routes.roles import routes as roles_routes
from .routes.user import pass_routes
from .routes.user import routes as user_routes
from .security.routes import routes as auth_routes

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        docs_url=None,
        lifespan=app_lifespan,
    )

    templates = Jinja2Templates(directory="static-files")
    app.templates = templates
    logger.info("Starting user service application...")
    project_path: Path = Path(__file__).parent.parent
    app.project_path = project_path
    app.version = project_path.joinpath(".version").read_text().strip()

    app.add_exception_handler(RequestValidationError, validation_handler)
    app.add_middleware(TimeIt, some_attribute="time")
    app.add_middleware(LogIt)
    # app.add_middleware(AuthenticationMiddleware)

    app.include_router(auth_routes)
    app.include_router(common_routes)
    app.include_router(user_routes)
    app.include_router(pass_routes)
    app.include_router(roles_routes)

    return app
