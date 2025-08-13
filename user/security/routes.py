from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .auth import Auth
from ..model.user import UserLogin, User
from ..service.roles import roles_service
from ..service.user import user_service

routes = APIRouter(tags=["Auth"])


@routes.post("/sign-in")
async def sign_in(user: UserLogin, svc: user_service, role_svc: roles_service, auth: Annotated[Auth, Depends(Auth)]):
    data = await auth.login(user, svc, role_svc)
    if data is None:
        return JSONResponse(status_code=401, content={"error": "Invalid credentials"})
    return JSONResponse(status_code=200, content=data)


@routes.post("/sign-up")
async def sign_up(user: User, svc: user_service) -> User:
    return await svc.create_user(user)
