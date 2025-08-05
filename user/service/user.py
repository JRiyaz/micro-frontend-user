from uuid import UUID

from ..model.item import ItemsBought
from ..model.user import User, UserEdit, UserPassword
from ..utils.constants import DEFAULT_USERS
from ..utils.utils import encrypt_password, is_encrypted


class UserService:
    def __init__(self):
        self._users: list[User] = [User(**usr) for usr in DEFAULT_USERS]
        for usr in self._users:
            if usr.username == "riyaz":
                usr.password = encrypt_password("pass")
                break

    async def get_users(self, skip: int, limit: int) -> list[User]:
        return self._users[skip:limit]

    async def get_user(self, user_id: UUID) -> User | None:
        # return next(filter(lambda usr: usr.id == user_id, self.users), None)
        for idx, usr in enumerate(self._users):
            if usr.id == user_id:
                return usr
        return None

    async def create_user(self, user: User) -> bool:
        self._users.append(user)
        return True

    async def update_user(self, user_id: UUID, user: UserEdit) -> bool:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return False
        db_user.__dict__.update(**user.model_dump(exclude_unset=True))
        return True

    async def delete_user(self, user_id: UUID) -> bool:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return False
        self._users.remove(db_user)
        return True

    async def patch_user(self, user_id: UUID, user: UserEdit) -> bool:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return False
        db_user.__dict__.update(**user.model_dump(exclude_unset=True))
        return True

    async def set_password(self, user_id: UUID, pwd: UserPassword) -> int:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return 404
        if db_user.password:
            return 204
        db_user.password = encrypt_password(pwd.password)
        return 200

    async def get_user_password(self, user_id: UUID) -> int | str:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return 404
        if not db_user.password:
            return 400
        if is_encrypted(db_user.password):
            return 200
        return "Invalid password"

    async def set_user_password(self, user_id: UUID, pwd: UserPassword):
        pass

    async def add_items(self, user_id: UUID, items: list[ItemsBought]) -> bool:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return False
        db_user.items.extend(items)
        return True

    async def remove_items(self, user_id: UUID, item_ids: list[ItemsBought]) -> bool:
        db_user: User = await self.get_user(user_id)
        if not db_user:
            return False
        for item in item_ids:
            db_user.items.remove(item)
        return True


service = UserService()
