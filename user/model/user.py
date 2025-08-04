from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class UserOut(BaseModel):
    username: str = Field(min_length=3, max_length=64)
    email: EmailStr
    firstName: str = Field(min_length=3, max_length=64)
    lastName: str = Field(min_length=3, max_length=64)


class UserPath(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=64)
    email: Optional[EmailStr] = None
    firstName: Optional[str] = Field(None, min_length=3, max_length=64)
    lastName: Optional[str] = Field(None, min_length=3, max_length=64)


class User(UserOut):
    id: UUID


class UserIn(User):
    password: Optional[str] = Field(min_length=3, max_length=64, exclude=True)


class UserCreate(UserIn):
    hash_password: str
