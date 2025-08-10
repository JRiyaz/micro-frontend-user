import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class TimeIt(BaseHTTPMiddleware):
    def __init__(self, app, some_attribute: str):
        super().__init__(app)
        self.some_attribute = some_attribute

    async def dispatch(self, request: Request, call_next):
        request.state.start_time = time.time()
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.3f} seconds"
        return response


class LogIt(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # start = time.time()
        response = await call_next(request)
        # duration = time.time() - start

        logger.info(
            {
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration": response.headers["X-Process-Time"],
                "client": request.client.host,
            }
        )

        return response
