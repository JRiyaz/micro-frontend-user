from uuid import UUID, uuid4

from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from ..model.generic import DetailMessage, Message
from ..model.user import User, UserOut, UserIn, UserPath
from ..utils.constants import USERS

user_routes = APIRouter(tags=["user"])


@user_routes.get("/users", response_model=list[User])
async def get_users():
    return USERS


@user_routes.get("/users/{user_id}", response_model=User, responses={404: {"model": DetailMessage}})
async def get_user(user_id: UUID):
    user: User = next(filter(lambda u: u.id == user_id, USERS), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found...")
    return user


@user_routes.post("/users", responses={201: {"model": Message}})
async def create_user(user: UserIn):
    user = User(id=uuid4(), **user.model_dump())
    USERS.append(user)
    return JSONResponse(status_code=201, content={"msg": "User created successfully..."})


@user_routes.put("/users/{user_id}", responses={200: {"model": Message}, 404: {"model": DetailMessage}})
async def update_user(user_id: UUID, user: UserOut):
    db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found...")
    update_usr: User = User(id=user_id, **user.model_dump())
    USERS.remove(db_user)
    USERS.append(update_usr)
    return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})


@user_routes.delete("/users/{user_id}", responses={404: {"model": Message}})
async def delete_user(user_id: UUID):
    db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found...")
    USERS.remove(db_user)
    return JSONResponse(status_code=200, content={"msg": "User deleted successfully..."})


@user_routes.patch("/users/{user_id}", responses={404: {"model": Message}})
async def patch_user(user_id: UUID, user: UserPath):
    db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found...")
    USERS.remove(db_user)
    update_usr: dict = db_user.model_dump()
    update_usr |= user.model_dump(exclude_unset=True)
    USERS.append(User(**update_usr))
    return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})
