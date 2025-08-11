from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import JSONResponse

from ..model import ForgotPassword, User, UserLogin, UserOptional, UserPassword
from ..model.general import JSONResp, NotFound, UserQuery
from ..security.auth import auth_security
from ..service.user import user_service

routes = APIRouter(tags=["User API's"], dependencies=[auth_security])


@routes.post("/login", dependencies=[])
async def login(user: UserLogin, svc: user_service):
    data = await svc.login(user)
    if data is None:
        return JSONResponse(status_code=401, content={"error": "Invalid credentials"})
    return JSONResponse(status_code=200, content=data)


# User routes
@routes.get("/users")
async def get_users(query: Annotated[UserQuery, Query()], svc: user_service, req: Request) -> list[User]:
    print("Request time is set to:", req.state.start_time)
    print("Auth token:", req.state.context)
    return await svc.get_users(query.skip, query.limit)


@routes.get("/users/{user_id}", responses={404: {"model": NotFound}})
async def get_user(user_id: UUID, svc: user_service) -> User:
    result: None | User = await svc.get_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@routes.post("/users")
async def create_user(user: User, svc: user_service) -> User:
    return await svc.create_user(user)


@routes.put("/users/{user_id}", responses={404: {"model": NotFound}})
async def update_user(user_id: UUID, user: User, svc: user_service) -> User:
    result: None | User = await svc.update_user(user_id, user)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@routes.patch("/users/{user_id}", responses={404: {"model": NotFound}})
async def patch_user(user_id: UUID, user: UserOptional, svc: user_service) -> User:
    result: None | User = await svc.path_user(user_id, user)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@routes.delete("/users/{user_id}", responses={404: {"model": NotFound}, 200: {"model": JSONResp}})
async def delete_user(user_id: UUID, svc: user_service):
    result: None | bool = await svc.delete_user(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=200, content={"msg": "User deleted successfully..."})


pass_routes = APIRouter(tags=["User Password API's"], dependencies=[auth_security])


@pass_routes.post("/users/{user_id}/check-password", responses={404: {"model": NotFound}, 200: {"model": JSONResp}})
async def check_password(user_id: UUID, svc: user_service):
    result: None | bool = await svc.is_password_set(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not result:
        return JSONResponse(status_code=200, content={"msg": "Password is not set"})
    return JSONResponse(status_code=200, content={"msg": "OK"})


@pass_routes.post("/users/{user_id}/password", responses={404: {"model": NotFound}, 200: {"model": JSONResp}})
async def create_password(user_id: UUID, usr_pass: UserPassword, svc: user_service):
    result: bool | None = await svc.create_password(user_id, usr_pass)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=200, content={"msg": "Password created successfully..."})


@pass_routes.post("/users/{user_id}/change-password", responses={404: {"model": NotFound}, 200: {"model": JSONResp}})
@pass_routes.post("/users/{user_id}/forgot-password", responses={404: {"model": NotFound}, 200: {"model": JSONResp}})
async def forgot_password(user_id: UUID, usr_pass: ForgotPassword, svc: user_service):
    result: bool = await svc.forgot_password(user_id, usr_pass)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not result:
        return JSONResponse(status_code=400, content={"msg": "Incorrect password"})
    return JSONResponse(status_code=200, content={"msg": "Password changed successfully..."})
