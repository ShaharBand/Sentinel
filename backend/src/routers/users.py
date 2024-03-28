from typing import TYPE_CHECKING

from fastapi import APIRouter

if TYPE_CHECKING:
    from src.dal.entities.user import User

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"description": "Not found"}})


@router.get("/")
async def read_users() -> list[User]:
    # TODO: Add logic to retrieve and return all users
    pass


@router.get("/{username}")
async def read_user(username: str) -> User:
    # TODO: Add logic to retrieve and return a user based on the provided username
    pass
