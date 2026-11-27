from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import UserModel
from src.schemas.data_transfer_objects import UserFullDto

from .base_db_repository import BaseDbRepository


class UserRepository(BaseDbRepository[UserModel, UserFullDto, UserFullDto]):
    """Репозиторий для работы с пользователями."""

    def __init__(self, async_db_session: AsyncSession):
        super().__init__(
            async_db_session=async_db_session,
            model_type=UserModel,
            full_schema_type=UserFullDto,
            short_schema_type=UserFullDto,
        )

    async def get_user_by_login(self, login: str) -> UserFullDto | None:
        """Получение пользователя по логину.

        :param login: Логин пользователя.
        :return: Полный DTO пользователя.
        """
        statement = select(UserModel).where(UserModel.login == login)
        result = await self.async_db_session.execute(statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return UserFullDto.model_validate(obj=model)

    async def update_last_login_at(self, user_id: int) -> None:
        """Обновление времени последнего входа.

        :param user_id: ID пользователя.
        """
        model = await self.async_db_session.get(UserModel, user_id)
        if model is None:
            return
        model.last_login_at = datetime.now().replace(microsecond=0)
        await self.async_db_session.flush()
