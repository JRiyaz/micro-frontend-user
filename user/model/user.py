from datetime import datetime
from enum import Enum
from typing import Any, Callable
from uuid import UUID, uuid4

from pydantic import EmailStr
from pydantic.json_schema import SkipJsonSchema
from sqlmodel import Enum as SQLEnum
from sqlmodel import Field, SQLModel


def enum_values(enum_class: type[Enum]) -> list[Callable[[], Any]]:
    return [member.value for member in enum_class]


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    MEMBER = "member"
    MANAGER = "manager"


class Gender(Enum):
    male = "male"
    female = "female"
    other = "other"
    unknown = "unknown"


class UserRoles(SQLModel, table=True):
    # __tablename__: str = "user_roles"

    id: int | None = Field(primary_key=True)
    role: Role = Field(sa_type=SQLEnum(Role, values_callable=enum_values))
    user_id: UUID = Field(foreign_key="user.id")

    def __repr__(self) -> str:
        return f"<UserRole(ID={self.id}, role={self.role}, user_id={self.user_id})>"


class UserOptional(SQLModel):
    username: str | None
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    gender: Gender | None


class User(UserOptional, table=True):
    # __tablename__: str = "users"

    id: SkipJsonSchema[UUID | None] = Field(default_factory=lambda: uuid4(), primary_key=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    email: EmailStr = Field(unique=True)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    gender: Gender = Field(sa_type=SQLEnum(Gender, values_callable=enum_values))
    status: SkipJsonSchema[bool] = Field(default=False, exclude=True)

    created_at: SkipJsonSchema[datetime] = Field(exclude=True)
    updated_at: SkipJsonSchema[datetime | None] = Field(default_factory=lambda: datetime.now(), exclude=True)

    def __repr__(self) -> str:
        return (
            f"<User(id: {self.id}, username: {self.username}, email: {self.email}, first_name: {self.first_name}, "
            f"last_name: {self.last_name}, gender: {self.gender}, status: {self.status})>"
        )
