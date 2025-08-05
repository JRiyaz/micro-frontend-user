from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from ..model.generic import DetailMessage, Message
from ..model.user import User, UserEdit, UserIn, UserPassword
from ..service.user import UserService

service = UserService()
user_routes = APIRouter(tags=["user"])


@user_routes.get("/users", response_model=list[User])
async def get_users(skip: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int | None, Query(ge=1, le=100)] = 100):
    return await service.get_users(skip, limit)


@user_routes.get("/users/{user_id}", response_model=User, responses={404: {"model": DetailMessage}})
async def get_user(user_id: UUID):
    user: User = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found...")
    return user


@user_routes.post("/users", responses={201: {"model": Message}})
async def create_user(user: UserIn):
    await service.create_user(user)
    return JSONResponse(status_code=201, content={"msg": "User created successfully..."})


@user_routes.put("/users/{user_id}", responses={200: {"model": Message}, 404: {"model": DetailMessage}})
async def update_user(user_id: UUID, user: UserEdit):
    if await service.update_user(user_id, user):
        return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})
    raise HTTPException(status_code=404, detail="User not found...")


@user_routes.delete("/users/{user_id}", responses={200: {"model": Message}, 404: {"model": Message}})
async def delete_user(user_id: UUID):
    if await service.delete_user(user_id):
        return JSONResponse(status_code=200, content={"msg": "User deleted successfully..."})
    raise HTTPException(status_code=404, detail="User not found...")


@user_routes.patch("/users/{user_id}", responses={200: {"model": Message}, 404: {"model": Message}})
async def patch_user(user_id: UUID, user: UserEdit):
    if await service.patch_user(user_id, user):
        return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})
    raise HTTPException(status_code=404, detail="User not found...")


@user_routes.post("/users/{user_id}/password", responses={200: {"model": Message}, 400: {"model": DetailMessage}})
async def set_password(user_id: UUID, pwd: UserPassword):
    status: int = await service.set_password(user_id, pwd)
    if status == 204:
        raise HTTPException(status_code=204, detail="Password already set...")
    elif status == 404:
        raise HTTPException(status_code=404, detail="User not found...")
    return JSONResponse(status_code=200, content={"msg": "Password set successfully..."})


@user_routes.get("/users/{user_id}/password", responses={200: {"model": Message}, 404: {"model": Message}})
async def get_user_password(user_id: UUID):
    resp: int | str = await service.get_user_password(user_id)
    if isinstance(resp, str):
        return JSONResponse(status_code=404, content={"msg": "Password is invalid, please set it correctly..."})
    elif resp == 404:
        raise HTTPException(status_code=404, detail="User not found...")
    elif resp == 400:
        return JSONResponse(status_code=400, content={"msg": "Password not set..."})
    return JSONResponse(status_code=200, content={"msg": "Password is already set..."})


@user_routes.put("/users/{user_id}/password", responses={200: {"model": Message}, 400: {"model": DetailMessage}})
async def set_user_password(user_id: UUID, pwd: UserPassword):
    return await service.set_user_password(user_id, pwd)
