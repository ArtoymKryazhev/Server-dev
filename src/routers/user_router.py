from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status

from src.controllers import UserController
from src.dependencies import get_user_controller
from src.schemas.data_transfer_objects import UserFullDto

user_router = APIRouter(
    prefix='/user',
    tags=['Пользователи'],
    deprecated=False,
    dependencies=None,
)


@user_router.get(
    '/many',
    summary='Список пользователей',
    response_model=List[UserFullDto],
    status_code=status.HTTP_200_OK,
)
async def get_user_many(
        user_controller: Annotated[UserController, Depends(get_user_controller)],
) -> List[UserFullDto]:
    """Получение списка пользователей."""
    return await user_controller.get_user_many()


@user_router.get(
    '/{user_id}',
    summary='Пользователь по идентификатору',
    response_model=UserFullDto,
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(
        user_controller: Annotated[UserController, Depends(get_user_controller)],
        user_id: int = Path(description='ID пользователя', ge=1, examples=[1]),
) -> UserFullDto:
    """Получение пользователя."""
    user = await user_controller.get_user_by_id(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')
    return user


@user_router.post(
    '',
    summary='Создание пользователя',
    response_model=UserFullDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
        user: UserFullDto,
        user_controller: Annotated[UserController, Depends(get_user_controller)],
) -> UserFullDto:
    """Создание пользователя."""
    return await user_controller.create_user(user=user)


@user_router.put(
    '/{user_id}',
    summary='Редактирование пользователя',
    response_model=UserFullDto,
    status_code=status.HTTP_200_OK,
)
async def update_user(
        user: UserFullDto,
        user_controller: Annotated[UserController, Depends(get_user_controller)],
        user_id: int = Path(description='ID пользователя', ge=1, examples=[1]),
) -> UserFullDto:
    """Редактирование пользователя."""
    updated = await user_controller.update_user(user_id=user_id, user=user)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')
    return updated


@user_router.delete(
    '/{user_id}',
    summary='Удаление пользователя',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
        user_controller: Annotated[UserController, Depends(get_user_controller)],
        user_id: int = Path(description='ID пользователя', ge=1, examples=[1]),
) -> None:
    """Удаление пользователя."""
    deleted = await user_controller.delete_user(user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')
