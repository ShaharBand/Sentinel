from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import PydanticObjectId

from src.dal.entities.user import User


class UserRepository:
    @staticmethod
    async def create_user(user_data: dict) -> User:
        new_user = User(**user_data)
        await new_user.insert()
        return new_user

    @staticmethod
    async def get_user_by_username(username: str) -> User:
        user = await User.find_one(User.username == username)
        return user

    @staticmethod
    async def get_user_by_uuid(user_uuid: PydanticObjectId) -> User:
        user = await User.get(user_uuid)
        return user

    @staticmethod
    async def update_user_password(user: User, new_password: str) -> bool:
        user.password = new_password
        await user.update()
        return True

    @staticmethod
    async def delete_user(user: User) -> bool:
        await user.delete()
        return True
