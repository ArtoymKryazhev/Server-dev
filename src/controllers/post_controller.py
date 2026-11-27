from typing import List
from typing import Optional

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostFullDto


class PostController(BaseControllerInterface):
    """Контроллер для работы с постами."""

    def __init__(self, post_repository: PostRepository):
        self._post_repository = post_repository

    async def get_post_by_id(self, post_id: int) -> Optional[PostFullDto]:
        """Получение поста по ID.

        :param post_id: ID поста.
        :return: Полный DTO поста.
        """
        return await self._post_repository.get_one_full_by_id(object_id=post_id)

    async def get_post_many(self) -> List[PostFullDto]:
        """Получение списка постов.

        :return: Список постов.
        """
        return await self._post_repository.get_many_full()

    async def create_post(self, post: PostFullDto) -> PostFullDto:
        """Создание поста.

        :param post: Данные поста.
        :return: Созданный пост.
        """
        return await self._post_repository.upsert(dto=post)

    async def update_post(self, post_id: int, post: PostFullDto) -> Optional[PostFullDto]:
        """Редактирование поста.

        :param post_id: ID поста.
        :param post: Новые данные поста.
        :return: Обновлённый пост.
        """
        existing = await self._post_repository.get_one_full_by_id(object_id=post_id)
        if existing is None:
            return None
        return await self._post_repository.upsert(dto=post.model_copy(update={'id': post_id}))

    async def delete_post(self, post_id: int) -> bool:
        """Удаление поста.

        :param post_id: ID поста.
        :return: Признак удаления.
        """
        return await self._post_repository.delete_one_by_id(object_id=post_id)
