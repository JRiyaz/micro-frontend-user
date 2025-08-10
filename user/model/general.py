from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(100, ge=0, le=100)


class NotFound(BaseModel):
    detail: str = "Not found"


class JSONResp(BaseModel):
    msg: str
