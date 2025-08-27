import logging

from fastapi import APIRouter, Query, Request, WebSocket, WebSocketDisconnect
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse

logger = logging.getLogger(__name__)

routes = APIRouter(tags=["common"], include_in_schema=False)

# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory=path), name="static")


html = """

"""

# Track connected clients
connected_clients = {}


@routes.get("/")
async def get(request: Request):
    # from fastapi.responses import HTMLResponse
    # return HTMLResponse(html)
    templates = request.app.templates
    client_host = request.client.host  # IP
    client_port = request.client.port  # Port
    client_info = f"{client_host}:{client_port}"
    return templates.TemplateResponse("chat.html", {"request": request, "client_info": client_info})


@routes.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, client: str = Query(None)):
    await websocket.accept()
    client_add = f"{websocket.client.host}:{websocket.client.port}"
    connected_clients[client] = websocket
    logger.info(f"WebSocket connected from: {client}")
    try:
        while True:
            data = await websocket.receive_text()
            for info, ws in connected_clients.items():
                await ws.send_text(f"{client} says: {data}")
    except WebSocketDisconnect:
        logger.warning(f"WebSocket disconnected from {client}")
        del connected_clients[client]


@routes.get("/docs")
async def docs() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="User-Service",
        swagger_favicon_url="/favicon.ico",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1, "deepLinking": False},
        # swagger_favicon_url="/static/favicon.png",
        # swagger_favicon_url=str(path.joinpath("favicon.png")),
    )


@routes.get("/favicon.ico")
async def favicon(req: Request) -> FileResponse:
    path = req.app.project_path.joinpath("static-files")
    return FileResponse(path.joinpath("favicon.ico"))
