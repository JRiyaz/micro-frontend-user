from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_handler(request: Request, exc: Exception | RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        # content="Data validation error",
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
