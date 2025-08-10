from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from ..config import config


class Security(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        try:
            http_auth = await super().__call__(request)
            token = http_auth.credentials
        except HTTPException:
            # Cookie for client app
            token = request.cookies.get(config.AUTH_COOKIE_NAME)
            if not token:
                if self.auto_error:
                    raise HTTPException(
                        status_code=401,
                        detail="Not authenticated",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
                token = None
        request.state.context = token
        return token
