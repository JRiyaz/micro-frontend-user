from uuid import UUID, uuid4

from ..model.user import User, UserIn, UserEdit, UserPassword, UserInfo
from ..utils.constants import DEFAULT_USERS
from ..utils.utils import encrypt_password, is_encrypted


class UserService:
    def __int__(self):
        self.__users: list[User] = [User(**usr) for usr in DEFAULT_USERS]
        for usr in self.__users:
            if usr.username == "riyaz":
                usr.password = encrypt_password("pass")
                break

    async def get_users(self) -> list[User]:
        return self.__users

    async def get_user(self, user_id: UUID) -> UserInfo:
        # return next(filter(lambda usr: usr.id == user_id, self.users), None)
        details: UserInfo = dict(user=None, index=-1)
        for idx, usr in enumerate(self.__users):
            if usr.id == user_id:
                details["index"] = idx
                details["user"] = usr
                break
        return details

    async def create_user(self, user: UserIn) -> bool:
        user = User(id=uuid4(), **user.model_dump())
        self.__users.append(user)
        return True

    async def update_user(self, user_id: UUID, user: UserIn) -> bool:
        usr_dtls = await self.get_user(user_id)
        db_user: User = await usr_dtls["user"]
        if not db_user:
            return False
        self.__users[usr_dtls["index"]].__dict__.update(**user.model_dump())
        return True

    async def delete_user(self, user_id: UUID) -> bool:
        usr_dtls = await self.get_user(user_id)
        db_user: User = await usr_dtls["user"]
        if not db_user:
            return False
        del self.__users[usr_dtls["index"]]
        return True

    async def patch_user(self, user_id: UUID, user: UserEdit) -> bool:
        usr_dtls = await self.get_user(user_id)
        db_user: User = await usr_dtls["user"]
        if not db_user:
            return False
        self.__users[usr_dtls["index"]].__dict__.update(**user.model_dump(exclude_unset=True))
        return True

    async def set_password(self, user_id: UUID, pwd: UserPassword) -> int:
        usr_dtls = await self.get_user(user_id)
        db_user: User = await usr_dtls["user"]
        if not db_user:
            return 404
        if db_user.password:
            return 401
        self.__users[usr_dtls["index"]].password = encrypt_password(pwd.password)
        return 200

    async def get_user_password(self, user_id: UUID) -> int | str:
        usr_dtls = await self.get_user(user_id)
        db_user: User = await usr_dtls["user"]
        if not db_user:
            return 404
        if not db_user.password:
            return 400
        if is_encrypted(db_user.password):
            return 200
        return "Invalid password"

    async def set_user_password(self, user_id: UUID, pwd: UserPassword):
        pass
