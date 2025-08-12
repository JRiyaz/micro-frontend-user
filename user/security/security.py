from typing import TYPE_CHECKING, Optional

from fastapi import Depends, Request
from fastapi.security import HTTPBearer

from .auth import Auth

if TYPE_CHECKING:
    pass


class Security(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        return await Auth.authenticate(request)
        # token = None
        # try:
        #     if auth := await super().__call__(request):
        #         token = auth.credentials
        # except HTTPException:
        #     # Cookie for client app
        #     token = request.cookies.get(config.AUTH_COOKIE_NAME)
        #     if not token and self.auto_error:
        #         raise HTTPException(
        #             status_code=401,
        #             detail="Not authenticated",
        #             headers={"WWW-Authenticate": "Bearer"},
        #         )
        # await Auth.authenticate(token=token, req=request)
        # request.state.context = token
        # return token


auth_security: Depends = Depends(Security(auto_error=True))
