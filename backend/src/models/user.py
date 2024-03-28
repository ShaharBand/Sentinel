from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.dal.entities.user import User

from src.dal.repositories.user import UserRepository


class UserModel:
    def __init__(self):
        self.user_repo = UserRepository()

    async def create_user(self, username: str, password: str) -> User:
        user_data = {
            'username': username,
            'password': password,
            # TODO: the rest here...
        }
        return await self.user_repo.create_user(**user_data)

    async def get_user_by_username(self, username: str) -> User:
        return await self.user_repo.get_user_by_username(username)

    async def update_user_password(self, username: str, new_password: str) -> bool:
        user = await self.get_user_by_username(username)
        if user:
            return await self.user_repo.update_user_password(user, new_password)
        return False

    async def delete_user(self, username: str) -> bool:
        user = await self.get_user_by_username(username)
        if user:
            await self.user_repo.delete_user(user)
            return True
        return False
