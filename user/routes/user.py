from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import JSONResponse

from ..model import User, UserOptional
from ..model.general import NotFound, UserQuery
from ..security.auth import Security
from ..service.user import user_service

routes = APIRouter(tags=["user"], dependencies=[Depends(Security(auto_error=True))])


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


@routes.delete("/users/{user_id}", responses={404: {"model": NotFound}, 200: {"model": JSONResponse}})
async def delete_user(user_id: UUID, svc: user_service):
    result: None | bool = await svc.delete_user(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=200, content={"msg": "User deleted successfully..."})
