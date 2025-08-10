from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from ..model import User
from ..model.general import UserQuery
from ..security.auth import Security
from ..service.user import user_service

routes = APIRouter(tags=["user"], dependencies=[Depends(Security(auto_error=True))])


@routes.get("/users")
def get_users(query: Annotated[UserQuery, Query()], svc: user_service, req: Request) -> list[User]:
    print("Request time is set to:", req.state.start_time)
    print("Auth token:", req.state.context)
    return svc.get_users(query.skip, query.limit)


@routes.post("/users")
def create_user(user: User, svc: user_service) -> User:
    return svc.create_user(user)
