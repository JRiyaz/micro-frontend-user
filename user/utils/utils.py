from typing import Any, Annotated

from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession


def get_auth_storage(req: Request):
    return req.state.auth_db


def get_db(req: Request) -> AsyncSession:
    return req.state.db_session


AuthDB = Annotated[Any, Depends(get_auth_storage, use_cache=False)]
DB = Annotated[AsyncSession, Depends(get_db, use_cache=False)]
