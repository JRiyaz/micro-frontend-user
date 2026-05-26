import re
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from user.utils.sanitizer import SanitizedStr

class UserRegister(BaseModel):
    username: SanitizedStr = Field(..., min_length=3, max_length=50)
    email: SanitizedStr
    password: str = Field(..., min_length=6)
    name: SanitizedStr = Field(..., min_length=1, max_length=100)
    company: SanitizedStr | None = Field(default=None, max_length=100)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if not re.match(r"^\S+@\S+\.\S+$", v):
            raise ValueError("Invalid email address format")
        return v

class UserLogin(BaseModel):
    username: SanitizedStr = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    name: str
    company: str | None
    role: str
    status: str
    join_date: datetime

    class Config:
        from_attributes = True  # Modern Pydantic v2 configuration (replaces orm_mode = True)

class UserRoleUpdate(BaseModel):
    role: SanitizedStr

    @field_validator("role")
    @classmethod
    def validate_role(cls, v: str) -> str:
        if v not in ("Admin", "Customer", "Agent"):
            raise ValueError("Role must be Admin, Customer, or Agent")
        return v
