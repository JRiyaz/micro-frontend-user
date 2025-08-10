from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from ..config import config


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
