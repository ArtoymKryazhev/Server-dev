from pydantic import Field

from src.schemas.common import BaseSchema


class LoginRequestSchema(BaseSchema):
    """Запрос для входа в систему."""

    login: str = Field(
        description='Почта пользователя',
        min_length=1,
        max_length=255,
        kw_only=True,
    )
    password: str = Field(
        description='Пароль пользователя',
        min_length=1,
        max_length=255,
        kw_only=True,
    )
