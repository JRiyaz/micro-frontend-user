import json
from base64 import urlsafe_b64encode
from datetime import datetime, timedelta
from hashlib import sha512
from hmac import compare_digest
from typing import TYPE_CHECKING, Annotated, Optional, Sequence
from uuid import uuid4

from cryptography.fernet import Fernet, InvalidToken
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer

from ..config import config
from ..model import User, UserLogin, UserOptional, UserRoles
from ..service.token import TokenService
from ..utils.string import get_unique_id

if TYPE_CHECKING:
    from ..service.roles import UserRolesService


class Crypt:
    secret_key = Fernet(config.AUTH_SECRET_KEY)

    @classmethod
    def hash_it(cls, password: str) -> str:
        hashed_pass, salt = cls.hash_password(password)
        return f"{hashed_pass.decode('utf-8')}:{salt.decode('utf-8')}"

    @classmethod
    def hash_password(cls, password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
        # Create random salt
        if not salt:
            salt: bytes = urlsafe_b64encode(uuid4().bytes)

        # Create sha with salt and password
        sha: bytes = sha512(password.encode("utf-8") + salt).digest()

        # Create hashed password
        hashed_pass: bytes = urlsafe_b64encode(sha)

        return hashed_pass, salt

    @classmethod
    def encrypt(cls, data: str) -> str:
        return cls.secret_key.encrypt(data.encode("utf-8")).decode("utf-8")

    @classmethod
    def decrypt(cls, data: str) -> str:
        return cls.secret_key.decrypt(data.encode("utf-8")).decode("utf-8")

    @classmethod
    def is_encrypted(cls, data: str) -> bool:
        try:
            cls.decrypt(data)
        except InvalidToken:
            return False
        else:
            return True

    @classmethod
    def compare_password(cls, db_pass: str, pass_in: str) -> bool:
        # Extract password and salt
        password, salt = db_pass.split(":")

        # Hash the incoming password
        pass_in_hash, _ = cls.hash_password(pass_in, salt.encode("utf-8"))

        return compare_digest(password.encode("utf-8"), pass_in_hash)


class Security(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        token = None
        try:
            if auth := await super().__call__(request):
                token = auth.credentials
        except HTTPException:
            # Cookie for client app
            token = request.cookies.get(config.AUTH_COOKIE_NAME)
            if not token and self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        request.state.context = token
        return token

    @classmethod
    async def login(cls, user: UserLogin, db_user: User, usr_roles_ser: "UserRolesService") -> dict | None:
        if not (db_user and db_user.is_active and db_user.password):
            return None

        if not Crypt.compare_password(db_user.password, user.password):
            return None

        user_roles: Sequence[UserRoles] = await usr_roles_ser.roles(db_user.id)
        user_fields: set[str] = set(UserOptional.model_fields.keys())
        expiry_time = datetime.now() + timedelta(minutes=config.AUTH_EXPIRATION_TIME)
        csrf_token = get_unique_id()
        data = {
            "user_data": db_user.model_dump(include=user_fields),
            "created_at": datetime.now(),
            "csrf": csrf_token,
            "expires_at": expiry_time,
        }
        roles = tuple(role.role.value for role in user_roles)
        data["user_data"]["roles"] = roles

        print(data)  # TODO: Remove this line
        auth_token: str = get_unique_id()
        # encrypt_data: str = Crypt.encrypt(json.dumps(data))
        #
        # print(encrypt_data)  # TODO: Remove this line
        #
        # TokenService().set(auth_token, encrypt_data)

        return {"auth_token": auth_token, "csrf_token": csrf_token}


auth_security: Depends = Depends(Security(auto_error=True))
