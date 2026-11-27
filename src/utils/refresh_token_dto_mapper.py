from datetime import datetime
from datetime import timedelta

from settings import app_settings
from src.schemas.data_transfer_objects import RefreshTokenFullDto


class RefreshTokenDtoMapper:
    """Сборка DTO refresh-токенов."""

    @staticmethod
    def map_from_user_id(user_id: int) -> RefreshTokenFullDto:
        """Сборка DTO refresh-токена с помощью id пользователя.

        :param user_id: ID пользователя.
        :return: DTO refresh-токена.
        """
        created_at = datetime.now().replace(microsecond=0)
        return RefreshTokenFullDto(
            user_id=user_id,
            expire_at=created_at + timedelta(minutes=app_settings.REFRESH_TOKEN_EXPIRES_MINUTES),
            created_at=created_at,
        )
