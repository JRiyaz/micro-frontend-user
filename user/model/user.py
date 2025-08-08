from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import EmailStr
from pydantic.json_schema import SkipJsonSchema
from sqlmodel import Enum as SQLEnum
from sqlmodel import Field, SQLModel


def enum_values(enum_class: type[Enum]) -> list:
    """Get values for enum."""
    return [status.value for status in enum_class]


def enum_value(enum_class: Enum) -> Any:
    """Get values for enum."""
    return enum_class.value


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    MEMBER = "member"
    MANAGER = "manager"


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    UNKNOWN = "unknown"


class UserRoles(SQLModel, table=True):
    id: int = Field(primary_key=True)
    role: Role = Field(SQLEnum(Role, values_callable=enum_values))
    user_id: UUID = Field(foreign_key="user.id")


class UserOptional(SQLModel):
    username: str | None
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    gender: Gender | None


class User(UserOptional, table=True):
    id: UUID | None = Field(default_factory=lambda: uuid4(), primary_key=True, exclude=True)
    username: str = Field(unique=True, min_length=3, max_length=50)
    email: EmailStr = Field(unique=True)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    gender: Gender = Field(SQLEnum(Gender, values_callable=enum_values))
    status: bool = Field(default=False)

    created_at: SkipJsonSchema[datetime] = Field(exclude=True)
    updated_at: SkipJsonSchema[datetime | None] = Field(default_factory=lambda: datetime.now(), exclude=True)

    def __repr__(self):
        return (
            f"<User(id: {self.id}, username: {self.username}, email: {self.email}, first_name: {self.first_name}, "
            f"last_name: {self.last_name}, gender: {self.gender}, status: {self.status})>"
        )
