from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ..model.generic import DetailMessage, Message
from ..model.user import User, UserEdit, UserIn
from ..utils.constants import USERS


class UserController:
    def __init__(self):
        self.user_router = APIRouter(tags=["user"])
        self.register_routes()

    def register_routes(self):
        self.user_router.get("/users", response_model=list[User])(self.get_users)
        self.user_router.get("/users/{user_id}", response_model=User, responses={404: {"model": DetailMessage}})(
            self.get_user
        )
        self.user_router.post("/users", responses={201: {"model": Message}})(self.create_user)
        self.user_router.put("/users/{user_id}", responses={200: {"model": Message}, 404: {"model": DetailMessage}})(
            self.update_user
        )
        self.user_router.delete("/users/{user_id}", responses={404: {"model": Message}})(self.delete_user)
        self.user_router.patch("/users/{user_id}", responses={404: {"model": Message}})(self.patch_user)

    async def get_users(self):
        return USERS

    async def get_user(self, user_id: UUID):
        user: User = next(filter(lambda u: u.id == user_id, USERS), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found...")
        return user

    async def create_user(self, user: UserIn):
        new_user = User(id=uuid4(), **user.model_dump())
        USERS.append(new_user)
        return JSONResponse(status_code=201, content={"msg": "User created successfully..."})

    async def update_user(self, user_id: UUID, user: UserIn):
        db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found...")
        update_usr: User = User(id=user_id, **user.model_dump())
        USERS.remove(db_user)
        USERS.append(update_usr)
        return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})

    async def delete_user(self, user_id: UUID):
        db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found...")
        USERS.remove(db_user)
        return JSONResponse(status_code=200, content={"msg": "User deleted successfully..."})

    async def patch_user(self, user_id: UUID, user: UserEdit):
        db_user: User = next(filter(lambda u: u.id == user_id, USERS), None)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found...")
        update_data = db_user.model_dump()
        update_data |= user.model_dump(exclude_unset=True)
        USERS.remove(db_user)
        USERS.append(User(**update_data))
        return JSONResponse(status_code=200, content={"msg": "User updated successfully..."})


# Create an instance and expose its router
user_routes = UserController().user_router
