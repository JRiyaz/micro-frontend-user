from typing import Annotated

from fastapi import APIRouter, Depends, Query

from ..model import User
from ..model.general import UserQuery
from ..security.auth import auth_token
from ..service.user import user_service

router = APIRouter(tags=["user"], dependencies=[Depends(auth_token)])


@router.get("/users")
def get_users(query: Annotated[UserQuery, Query()], svc: user_service) -> list[User]:
    return svc.get_users(query.skip, query.limit)


@router.post("/users")
def create_user(user: User, svc: user_service, token: auth_token) -> User:
    return svc.create_user(user)
