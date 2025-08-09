from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer

auth_scheme = HTTPBearer()
auth_token = Annotated[str, Depends(auth_scheme)]
