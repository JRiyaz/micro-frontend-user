from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse

from .db import create_db_tables
from .exceptions import validation_handler
from .routes.user import router as user_router


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        docs_url=None,
    )
    user_service_path: Path = Path(__file__).parent.parent
    version: str = user_service_path.joinpath(".version").read_text()
    app.version = version.strip()

    # from fastapi.staticfiles import StaticFiles
    # app.mount("/static", StaticFiles(directory=path), name="static")

    @app.on_event("startup")
    def startup_event() -> None:
        create_db_tables()

    @app.get("/docs", include_in_schema=False)
    def docs() -> HTMLResponse:
        return get_swagger_ui_html(
            openapi_url="/openapi.json",
            title="User-Service",
            swagger_favicon_url="/favicon.ico",
            swagger_ui_parameters={"defaultModelsExpandDepth": -1, "deepLinking": False},
            # swagger_favicon_url="/static/favicon.png",
            # swagger_favicon_url=str(path.joinpath("favicon.png")),
        )

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon() -> FileResponse:
        path = user_service_path.joinpath("static-files")
        return FileResponse(path.joinpath("favicon.ico"))

    app.add_exception_handler(RequestValidationError, validation_handler)

    app.include_router(user_router)

    return app
