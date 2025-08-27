from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..model.user import User, UserLogin
from ..service.roles import RolesSvc
from ..service.user import UserSrv
from .auth import Auth

routes = APIRouter(tags=["Auth"])


@routes.post("/sign-in")
async def sign_in(user: UserLogin, svc: UserSrv, role_svc: RolesSvc, auth: Annotated[Auth, Depends(Auth)]):
    data = await auth.login(user, svc, role_svc)
    if data is None:
        return JSONResponse(status_code=401, content={"error": "Invalid credentials"})
    res = JSONResponse(status_code=200, content=data)
    res.set_cookie(key="csrf_token", value=data["csrf_token"], secure=True, samesite="strict", path="/")
    res.set_cookie(key="auth_token", value=data["auth_token"], httponly=True, secure=True, samesite="strict", path="/")
    return res


@routes.post("/sign-up")
async def sign_up(user: User, svc: UserSrv) -> User:
    return await svc.create_user(user)
