import json
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Sequence

from fastapi import HTTPException, Request

from .utils import Crypt
from ..config import config
from ..database.db import Storage
from ..model import Gender, User, UserLogin, UserOptional, UserRoles
from ..utils.constants import CSRF_METHODS
from ..utils.string import get_unique_id

if TYPE_CHECKING:
    from ..service.roles import UserRolesService
    from ..service.user import UserService


class Auth:
    def __init__(self, store: Storage):
        self.store = store

    async def login(self, user: UserLogin, svc: "UserService", role_svc: "UserRolesService"):
        # Fetch the User
        db_user: User = await svc.get_user(user.email)
        if db_user is None:
            return db_user

        if not (db_user and db_user.is_active and db_user.password):
            return None

        if not Crypt.compare_password(db_user.password, user.password):
            return None

        user_roles: Sequence[UserRoles] = await role_svc.roles(db_user.id)
        user_fields: set[str] = set(UserOptional.model_fields.keys())
        expiry_time = datetime.now() + timedelta(minutes=config.AUTH_EXPIRATION_TIME)
        csrf_token = get_unique_id()
        data = {
            "user_data": db_user.model_dump(include=user_fields),
            "created_at": datetime.now().isoformat(),
            "csrf": csrf_token,
            "expires_at": expiry_time.isoformat(),
        }
        gender: Gender = data["user_data"]["gender"]
        data["user_data"]["gender"] = gender.value
        roles = tuple(role.role.value for role in user_roles)
        data["user_data"]["roles"] = roles

        auth_token: str = get_unique_id()
        encrypt_data: str = Crypt.encrypt(json.dumps(data))
        await self.store.set(auth_token, encrypt_data, config.AUTH_EXPIRATION_TIME)

        return {"auth_token": auth_token, "csrf_token": csrf_token}

    @classmethod
    async def authenticate(cls, req: Request) -> str:
        cls.req = req
        cls.store: Storage = cls.req.app.auth_storage

        if token := req.cookies.get(config.AUTH_COOKIE_NAME):
            if req.method in CSRF_METHODS:
                data: dict = await cls.validate_token_and_csrf(token)
            else:
                data: dict = await cls.validate_token(token)
        elif bearer := req.headers.get("Authorization"):
            if not bearer.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Signature verification failed")
            bearer, _, token = bearer.partition(" ")
            data: dict = await cls.validate_token(token)
        else:
            raise HTTPException(status_code=401, detail="Token not found")
        req.state.context = data
        req.state.is_authenticated = True
        req.state.token = token
        await cls.store.set_expire(token, config.AUTH_EXPIRATION_TIME)
        return token

    @classmethod
    async def validate_token(cls, token: str) -> dict:
        enc_token = await cls.store.get(token)
        if enc_token is None:
            raise HTTPException(status_code=401, detail="Token has expired")
        return json.loads(Crypt.decrypt(enc_token))

    @classmethod
    async def validate_token_and_csrf(cls, cookie: str) -> dict:
        csrf: str = cls.req.cookies.get(config.AUTH_COOKIE_CSRF)
        if not csrf:
            raise HTTPException(status_code=401, detail="CSRF token not found")
        user_data: dict = await cls.validate_token(cookie)
        if not Crypt.compare_password(user_data["csrf"], csrf):
            raise HTTPException(status_code=401, detail="CSRF token incorrect")
        return user_data
