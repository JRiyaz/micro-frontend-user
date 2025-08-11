from base64 import urlsafe_b64encode
from hashlib import sha512
from hmac import compare_digest
from typing import Optional
from uuid import uuid4

from cryptography.fernet import Fernet, InvalidToken
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer

from ..config import config


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


auth_security: Depends = Depends(Security(auto_error=True))
