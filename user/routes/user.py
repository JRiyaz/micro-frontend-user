from fastapi import APIRouter

from ..model import User
from ..service.user import UsrService

router = APIRouter(tags=["user"])


@router.get("/users")
def get_users(svc: UsrService, skip: int = 0, limit: int = 100) -> list[User]:
    return svc.get_users(skip, limit)


@router.post("/users")
def create_user(svc: UsrService, user: User) -> User:
    return svc.create_user(user)
