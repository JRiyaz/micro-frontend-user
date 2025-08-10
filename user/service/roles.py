from typing import Annotated, Sequence
from uuid import UUID

from fastapi import Depends
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.selectable import SelectBase
from sqlmodel import select

from ..database.db import SessionDep
from ..model import Role, UserRoles


class UserRolesService:
    def __init__(self, db: SessionDep):
        self.db: AsyncSession = db

    # UserRoles routes
    async def roles(self, user_id: UUID) -> Sequence[UserRoles]:
        # Fetch UserRoles
        stmt: SelectBase[UserRoles] = select(UserRoles).where(UserRoles.user_id == user_id)
        result: Result[tuple[UserRoles]] = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_roles(self, user_id: UUID) -> list[Role] | None:
        # Fetch UserRoles
        user_roles: Sequence[UserRoles] = await self.roles(user_id)

        if not user_roles:
            return None

        # Collect only Roles
        roles = [Role(role.role) for role in user_roles]
        return roles

    async def update_roles(self, user_id: UUID, roles: list[Role]) -> list[Role] | None:
        # Fetch User Roles
        db_roles: list[Role] | None = await self.get_roles(user_id)

        if db_roles is None:
            return db_roles

        # Filter only unique values
        roles: set[Role] = set(roles)

        # Filter for duplicate Roles
        filtered_roles: list[Role] = [role for role in roles if role not in db_roles]

        # Insert roles into DB
        if filtered_roles:
            user_roles: list[UserRoles] = [UserRoles(role=role, user_id=user_id) for role in filtered_roles]
            self.db.add_all(user_roles)
            await self.db.commit()

        # Append the inserted roles to DB roles instead of fetching again
        db_roles.extend(filtered_roles)
        return db_roles

    async def delete_roles(self, user_id: UUID, roles: list[Role]) -> list[Role] | int | None:
        # Fetch UserRoles
        user_roles: Sequence[UserRoles] = await self.roles(user_id)
        if not user_roles:
            return None

        if len(user_roles) == 1:
            return 1

        # Get only unique roles
        roles: set[Role] = set(roles)

        # Map the UserRoles to get only roles
        mapped_roles: dict[Role, UserRoles] = {role.role: role for role in user_roles}

        # Filter the roles that are present in DB
        filtered_roles: list[Role] = [role for role in roles if role in mapped_roles]

        for role in filtered_roles:
            await self.db.delete(mapped_roles[role])
        await self.db.commit()

        # Instead of query again for the updated roles, remove the roles deleted from DB
        return list(set(mapped_roles.keys()).difference(roles))


roles_service = Annotated[UserRolesService, Depends(UserRolesService)]
