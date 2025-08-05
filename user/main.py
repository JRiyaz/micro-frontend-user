from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, JSONResponse

from .routes.user import user_routes


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="User-Service",
        description="Service for managing user accounts and profiles",
        version="1.0.0",
        docs_url=None,
    )
    path = Path(__file__).parent.parent.joinpath("static-files")

    # from fastapi.staticfiles import StaticFiles
    # app.mount("/static", StaticFiles(directory=path), name="static")

    @app.get("/docs", include_in_schema=False)
    def docs():
        return get_swagger_ui_html(
            openapi_url="/openapi.json",
            title="User-Service",
            swagger_favicon_url="/favicon.ico",
            swagger_ui_parameters={"defaultModelsExpandDepth": -1, "deepLinking": False},
            # swagger_favicon_url="/static/favicon.png",
            # swagger_favicon_url=str(path.joinpath("favicon.png")),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            # content="Data validation error",
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon():
        return FileResponse(path.joinpath("favicon.ico"))

    app.include_router(user_routes)

    return app
