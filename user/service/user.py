from datetime import datetime
from typing import Annotated, Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.selectable import SelectBase
from sqlmodel import select
from sqlmodel.sql.expression import SelectOfScalar

from ..database.db import SessionDep
from ..model import Role, User, UserOptional, UserRoles
from ..utils.string import is_valid_email, is_valid_uuid


class UserService:
    def __init__(self, db: SessionDep):
        self.db: AsyncSession = db

    async def get_user_by_email(self, email: str) -> User | None:
        stmt: SelectBase[User] = select(User).where(User.email == email)
        result: Result[tuple[User]] = await self.db.execute(stmt)
        return result.first()

    async def get_user_by_username(self, username: str) -> User | None:
        stmt: SelectBase[User] = select(User).where(User.username == username)
        result: Result[tuple[User]] = await self.db.execute(stmt)
        return result.first()

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        return await self.db.get(User, user_id)

    async def get_user(self, data: str | UUID) -> User | None:
        if is_valid_uuid(data):
            return await self.get_user_by_id(data)
        elif is_valid_email(data):
            return await self.get_user_by_email(data)
        return await self.get_user_by_username(data)

    async def get_users(self, skip: int = 0, limit: int = 100) -> Sequence[User]:
        stmt: SelectOfScalar = select(User).offset(skip).limit(limit)
        result: Result[tuple[User]] = await self.db.execute(stmt)
        return result.scalars().all()

    async def create_user(self, user: User) -> User:
        # Update created_at
        user.created_at = datetime.now()

        # Add user to DB
        self.db.add(user)
        await self.db.commit()
        # Refresh user with DB values
        await self.db.refresh(user)

        # Create USER role for user
        role: UserRoles = UserRoles(role=Role.USER, user_id=user.id)

        # Save the role to DB
        self.db.add(role)
        await self.db.commit()
        return user

    async def update_user(self, user_id: UUID, user: User) -> User | None:
        # Fetch the User
        db_user: User = await self.get_user_by_id(user_id)
        if not db_user:
            return None

        # Update the User details
        user_data: dict = UserOptional.model_fields.keys()
        db_user.updated_at = datetime.now()
        for field in user_data:
            setattr(db_user, field, getattr(user, field))

        # Commit the changes
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def path_user(self, user_id: UUID, user: UserOptional) -> User | None:
        # Fetch the User
        db_user: User = await self.get_user_by_id(user_id)
        if not db_user:
            return None

        # Update the User details
        user_data: dict = user.model_dump(exclude_unset=True)
        db_user.updated_at = datetime.now()
        for key, value in user_data.items():
            setattr(db_user, key, value)

        # Commit the changes
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def delete_user(self, user_id: UUID) -> bool | None:
        # Fetch the User
        db_user: User | None = await self.get_user_by_id(user_id)
        if not db_user:
            return None

        # Delete the User
        await self.db.delete(db_user)
        await self.db.commit()
        return True


user_service = Annotated[UserService, Depends(UserService)]
