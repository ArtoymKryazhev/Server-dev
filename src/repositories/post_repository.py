from typing import List
from typing import Optional

from src.interfaces.repositories import BaseRepositoryInterface
from src.schemas.data_transfer_objects import PostFullDto


class PostRepository(BaseRepositoryInterface):
    """Репозиторий для работы с постами."""

    def __init__(self, posts: List[PostFullDto]):
        self._posts = posts

    async def get_post_by_id(self, post_id: int) -> Optional[PostFullDto]:
        """Получение поста по его ID.

        :param post_id: ID поста.
        :return: Полный DTO поста.
        """
        for post in self._posts:
            if post.id == post_id:
                return post
        return None

    async def get_post_many(self) -> List[PostFullDto]:
        """Получение списка полных DTO постов.

        :return: Список полных DTO постов.
        """
        return self._posts

    async def create_post(self, post: PostFullDto) -> PostFullDto:
        """Создание поста.

        :param post: Данные поста.
        :return: Созданный пост.
        """
        next_id = max((item.id or 0 for item in self._posts), default=0) + 1
        created = post.model_copy(update={'id': next_id})
        self._posts.append(created)
        return created

    async def update_post(self, post_id: int, post: PostFullDto) -> Optional[PostFullDto]:
        """Редактирование поста.

        :param post_id: ID поста.
        :param post: Новые данные поста.
        :return: Обновлённый пост.
        """
        for index, item in enumerate(self._posts):
            if item.id == post_id:
                updated = post.model_copy(update={'id': post_id})
                self._posts[index] = updated
                return updated
        return None

    async def delete_post(self, post_id: int) -> bool:
        """Удаление поста.

        :param post_id: ID поста.
        :return: Признак удаления.
        """
        for index, item in enumerate(self._posts):
            if item.id == post_id:
                del self._posts[index]
                return True
        return False
