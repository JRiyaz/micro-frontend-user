from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Callable, Self
from uuid import UUID, uuid4

from pydantic import (
    BaseModel,
    EmailStr,
    ValidatorFunctionWrapHandler,
    WrapValidator,
    model_validator,
)
from pydantic import Field as PydanticField
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


def validate_gender(value: Any, handler: ValidatorFunctionWrapHandler) -> Gender:
    if isinstance(value, Gender):
        return value
    if isinstance(value, str):
        try:
            return Gender(value)
        except ValueError:
            raise ValueError(f"Gender value '{value}' is invalid.")
    raise TypeError("Gender must be a string or a Gender enum member")


class UserRoles(SQLModel, table=True):
    # __tablename__: str = "user_roles"

    id: int | None = Field(primary_key=True)
    role: Role = Field(sa_type=SQLEnum(Role, values_callable=enum_values))
    user_id: UUID = Field(foreign_key="user.id")

    def __repr__(self) -> str:
        return f"<UserRole(ID={self.id}, role={self.role}, user_id={self.user_id})>"


class UserLogin(BaseModel):
    user_id: EmailStr | UUID | str
    password: str


class UserPassword(BaseModel):
    password: str = Field(min_length=3, max_length=64)
    confirm_password: str = Field(min_length=3, max_length=64)

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


class ChangePassword(UserPassword):
    old_password: str = Field(min_length=3, max_length=64)

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password == self.old_password:
            raise ValueError("Old and new passwords should not be same")
        return self


class UserOptional(SQLModel):
    mobile_no: str | None = PydanticField(None, pattern=r"^[6789]\d{9}$", validate_default=False)
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    gender: Gender | None


class User(UserOptional, table=True):
    # __tablename__: str = "users"

    id: SkipJsonSchema[UUID | None] = Field(default_factory=lambda: uuid4(), primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    mobile_no: str = Field(unique=True, index=True, max_length=10)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    gender: Annotated[
        Gender | str, Field(sa_type=SQLEnum(Gender, values_callable=enum_values)), WrapValidator(validate_gender)
    ]
    is_active: SkipJsonSchema[bool] = Field(default=False, exclude=True)
    password: SkipJsonSchema[str | None] = Field(default=None, exclude=True)

    created_at: SkipJsonSchema[datetime] = Field(exclude=True)
    updated_at: SkipJsonSchema[datetime | None] = Field(default_factory=lambda: datetime.now(), exclude=True)

    def __repr__(self) -> str:
        return (
            f"<User(id: {self.id}, mobile_no: {self.mobile_no}, email: {self.email}, first_name: {self.first_name}, "
            f"last_name: {self.last_name}, gender: {self.gender}, status: {self.is_active})>"
        )
