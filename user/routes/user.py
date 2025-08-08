from fastapi import APIRouter

user_router = APIRouter(tags=["user"])


@user_router.get("/users")
async def get_users():
    pass
