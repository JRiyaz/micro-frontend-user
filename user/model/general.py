from pydantic import BaseModel, Field, RootModel


class UserQuery(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(100, ge=0, le=100)


class NotFound(BaseModel):
    detail: str = "Not found"


class Tokens(BaseModel):
    auth_token: str
    csrf_token: str


class JSONResp(BaseModel):
    msg: str


class Root(RootModel):
    pass
