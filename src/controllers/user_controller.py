from typing import List
from typing import Optional

from passlib.context import CryptContext

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import UserRepository
from src.schemas.data_transfer_objects import UserFullDto


class UserController(BaseControllerInterface):
    """Контроллер для работы с пользователями."""

    def __init__(self, user_repository: UserRepository, password_context: CryptContext):
        self._user_repository = user_repository
        self._password_context = password_context

    async def get_user_by_id(self, user_id: int) -> Optional[UserFullDto]:
        """Получение пользователя по ID.

        :param user_id: ID пользователя.
        :return: Полный DTO пользователя.
        """
        return await self._user_repository.get_one_full_by_id(object_id=user_id)

    async def get_user_many(self) -> List[UserFullDto]:
        """Получение списка пользователей.

        :return: Список пользователей.
        """
        return await self._user_repository.get_many_full()

    async def create_user(self, user: UserFullDto) -> UserFullDto:
        """Создание пользователя.

        :param user: Данные пользователя.
        :return: Созданный пользователь.
        """
        hashed = user.model_copy(update={'password': self._password_context.hash(user.password)})
        return await self._user_repository.upsert(dto=hashed)

    async def update_user(self, user_id: int, user: UserFullDto) -> Optional[UserFullDto]:
        """Редактирование пользователя.

        :param user_id: ID пользователя.
        :param user: Новые данные пользователя.
        :return: Обновлённый пользователь.
        """
        existing = await self._user_repository.get_one_full_by_id(object_id=user_id)
        if existing is None:
            return None
        password = user.password
        if password != existing.password:
            password = self._password_context.hash(password)
        return await self._user_repository.upsert(
            dto=user.model_copy(update={'id': user_id, 'password': password}),
        )

    async def delete_user(self, user_id: int) -> bool:
        """Удаление пользователя.

        :param user_id: ID пользователя.
        :return: Признак удаления.
        """
        return await self._user_repository.delete_one_by_id(object_id=user_id)
