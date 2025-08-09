from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(100, ge=0, le=100)
