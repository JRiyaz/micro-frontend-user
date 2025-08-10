from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse

routes = APIRouter(tags=["common"])


# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory=path), name="static")


@routes.get("/docs", include_in_schema=False)
def docs() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="User-Service",
        swagger_favicon_url="/favicon.ico",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1, "deepLinking": False},
        # swagger_favicon_url="/static/favicon.png",
        # swagger_favicon_url=str(path.joinpath("favicon.png")),
    )


@routes.get("/favicon.ico", include_in_schema=False)
async def favicon(req: Request) -> FileResponse:
    path = req.app.project_path.joinpath("static-files")
    return FileResponse(path.joinpath("favicon.ico"))
