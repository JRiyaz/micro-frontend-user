from datetime import datetime, UTC
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    name: str = Field(nullable=False)
    company: str | None = Field(default=None)
    role: str = Field(default="Customer", nullable=False)  # Customer, Admin, Agent
    status: str = Field(default="Active", nullable=False)  # Active, Suspended
    join_date: datetime = Field(default_factory=lambda: datetime.now(UTC), nullable=False)

class AuditLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, index=True)
    username: str | None = Field(default=None)
    action: str = Field(nullable=False)  # LOGIN, REGISTER, UPDATE_ROLE, UPDATE_PROFILE
    resource: str = Field(nullable=False)  # Users, Authentication, Roles
    details: str = Field(nullable=False)  # Detailed log description
    ip_address: str | None = Field(default=None)
    correlation_id: str | None = Field(default=None)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC), nullable=False)
