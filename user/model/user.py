from typing import Self, TypedDict
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, model_validator


class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=64)
    email: EmailStr
    firstName: str = Field(min_length=3, max_length=64)
    lastName: str = Field(min_length=3, max_length=64)
    password: str | None = Field(None, min_length=3, exclude=True)


class UserEdit(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=64, examples=["username"])
    email: EmailStr | None = None
    firstName: str | None = Field(None, min_length=3, max_length=64, examples=["firstName"])
    lastName: str | None = Field(None, min_length=3, max_length=64, examples=["lastName"])


class User(UserIn):
    id: UUID


class UserInfo(TypedDict):
    user: User | None
    index: int


class UserPassword(BaseModel):
    password: str = Field(min_length=3, max_length=64)
    confirm_password: str = Field(min_length=3, max_length=64)

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
