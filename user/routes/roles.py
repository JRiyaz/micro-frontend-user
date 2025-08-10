from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..model import Role
from ..model.general import NotFound
from ..security.auth import auth_security
from ..service.roles import roles_service

routes = APIRouter(tags=["User Roles API's"], dependencies=[auth_security])


# User Roles routes
# @roles_routes.get("/users/roles/{user_id}", responses={404: {"model": NotFound}})
@routes.get("/roles/{user_id}", responses={404: {"model": NotFound}})
async def get_user_roles(user_id: UUID, svc: roles_service) -> list[Role]:
    result: list[Role] | None = await svc.get_roles(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@routes.post("/roles/{user_id}", responses={404: {"model": NotFound}})
async def update_user_roles(user_id: UUID, roles: list[Role], svc: roles_service) -> list[Role]:
    result: list[Role] | None = await svc.update_roles(user_id, roles)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@routes.delete("/roles/{user_id}", responses={404: {"model": NotFound}, 400: {"model": NotFound}})
async def delete_user_roles(user_id: UUID, roles: list[Role], svc: roles_service) -> list[Role]:
    result: list[Role] | int | None = await svc.delete_roles(user_id, roles)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    elif result == 1:
        raise HTTPException(status_code=400, detail="Cannot delete role as User has only one role.")
    return result
