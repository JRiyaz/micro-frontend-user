from datetime import datetime
from typing import Annotated, Sequence

from fastapi import Depends
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlmodel.sql.expression import SelectOfScalar

from ..database.db import SessionDep
from ..model import Role, User, UserRoles


class UserService:
    def __init__(self, db: SessionDep):
        self.db: AsyncSession = db

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


user_service = Annotated[UserService, Depends(UserService)]
