from datetime import datetime
from typing import Sequence, Annotated

from fastapi import Depends
from sqlmodel import Session, select
from sqlmodel.sql.expression import SelectOfScalar

from ..db import SessionDep
from ..model import Role, User, UserRoles


class UserService:
    def __init__(self, db: SessionDep):
        self.db: Session = db

    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        stmt: SelectOfScalar = select(User).offset(skip).limit(limit)
        users: Sequence[User] = self.db.exec(stmt).all()
        return list(users)

    def create_user(self, user: User) -> User:
        # Update created_at
        user.created_at = datetime.now()

        # Add user to DB
        self.db.add(user)
        self.db.commit()
        # Refresh user with DB values
        self.db.refresh(user)

        # Create USER role for user
        role: UserRoles = UserRoles(role=Role.USER, user_id=user.id)

        # Save the role to DB
        self.db.add(role)
        self.db.commit()
        return user


UsrService = Annotated[UserService, Depends(UserService)]
