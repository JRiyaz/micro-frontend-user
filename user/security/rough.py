from typing import Annotated, Optional

from fastapi import HTTPException, Request, status
from fastapi.openapi.models import HTTPBase
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param


class OptionalHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        try:
            r = await super().__call__(request)
            token = r.credentials
        except HTTPException as ex:
            assert ex.status_code == status.HTTP_403_FORBIDDEN, ex
            token = None
        return token


class HTTPBearer(HTTPBase):
    """
    HTTP Bearer token authentication.

    ## Usage

    Create an instance object and use that object as the dependency in `Depends()`.

    The dependency result will be an `HTTPAuthorizationCredentials` object containing
    the `scheme` and the `credentials`.

    ## Example

    ```python
    from typing import Annotated

    from fastapi import Depends, FastAPI
    from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

    app = FastAPI()

    security = HTTPBearer()


    @app.get("/users/me")
    def read_current_user(
        credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
    ):
        return {"scheme": credentials.scheme, "credentials": credentials.credentials}
    ```
    """

    def __init__(
        self,
        *,
        bearerFormat: Annotated[Optional[str], Doc("Bearer token format.")] = None,
        scheme_name: Annotated[
            Optional[str],
            Doc(
                """
                    Security scheme name.

                    It will be included in the generated OpenAPI (e.g. visible at `/docs`).
                    """
            ),
        ] = None,
        description: Annotated[
            Optional[str],
            Doc(
                """
                    Security scheme description.

                    It will be included in the generated OpenAPI (e.g. visible at `/docs`).
                    """
            ),
        ] = None,
        auto_error: Annotated[
            bool,
            Doc(
                """
                    By default, if the HTTP Bearer token is not provided (in an
                    `Authorization` header), `HTTPBearer` will automatically cancel the
                    request and send the client an error.

                    If `auto_error` is set to `False`, when the HTTP Bearer token
                    is not available, instead of erroring out, the dependency result will
                    be `None`.

                    This is useful when you want to have optional authentication.

                    It is also useful when you want to have authentication that can be
                    provided in one of multiple optional ways (for example, in an HTTP
                    Bearer token or in a cookie).
                    """
            ),
        ] = True,
    ):
        self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        authorization = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated")
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication credentials",
                )
            else:
                return None
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)
