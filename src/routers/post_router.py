from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status

from src.controllers import PostController
from src.dependencies import get_post_controller
from src.schemas.data_transfer_objects import PostFullDto

post_router = APIRouter(
    prefix='/post',
    tags=['Посты'],
    deprecated=False,
    dependencies=None,
)


@post_router.get(
    '/many',
    summary='Список постов',
    response_model=List[PostFullDto],
    status_code=status.HTTP_200_OK,
)
async def get_post_many(
        post_controller: Annotated[PostController, Depends(get_post_controller)],
) -> List[PostFullDto]:
    """Получение списка постов."""
    return await post_controller.get_post_many()


@post_router.get(
    '/{post_id}',
    summary='Пост по идентификатору',
    response_model=PostFullDto,
    status_code=status.HTTP_200_OK,
)
async def get_post_by_id(
        post_controller: Annotated[PostController, Depends(get_post_controller)],
        post_id: int = Path(description='ID поста', ge=1, examples=[1]),
) -> PostFullDto:
    """Получение информации о посте."""
    post = await post_controller.get_post_by_id(post_id=post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пост не найден')
    return post


@post_router.post(
    '',
    summary='Создание поста',
    response_model=PostFullDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_post(
        post: PostFullDto,
        post_controller: Annotated[PostController, Depends(get_post_controller)],
) -> PostFullDto:
    """Создание поста."""
    return await post_controller.create_post(post=post)


@post_router.put(
    '/{post_id}',
    summary='Редактирование поста',
    response_model=PostFullDto,
    status_code=status.HTTP_200_OK,
)
async def update_post(
        post: PostFullDto,
        post_controller: Annotated[PostController, Depends(get_post_controller)],
        post_id: int = Path(description='ID поста', ge=1, examples=[1]),
) -> PostFullDto:
    """Редактирование поста."""
    updated = await post_controller.update_post(post_id=post_id, post=post)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пост не найден')
    return updated


@post_router.delete(
    '/{post_id}',
    summary='Удаление поста',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_post(
        post_controller: Annotated[PostController, Depends(get_post_controller)],
        post_id: int = Path(description='ID поста', ge=1, examples=[1]),
) -> None:
    """Удаление поста."""
    deleted = await post_controller.delete_post(post_id=post_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пост не найден')
