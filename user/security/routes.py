from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..model.user import UserLogin
from ..service.roles import roles_service
from ..service.user import user_service
from .auth import Auth

routes = APIRouter(tags=["Auth"])


@routes.post("/login")
async def login(user: UserLogin, svc: user_service, role_svc: roles_service, auth: Annotated[Auth, Depends(Auth)]):
    data = await auth.login(user, svc, role_svc)
    if data is None:
        return JSONResponse(status_code=401, content={"error": "Invalid credentials"})
    return JSONResponse(status_code=200, content=data)
