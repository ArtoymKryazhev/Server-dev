from pydantic import Field

from src.schemas.common import MixinIdSchema
from src.schemas.common import MixinSoftDeleteSchema


class UserFullDto(MixinIdSchema, MixinSoftDeleteSchema):
    """Полный DTO пользователя."""

    username: str = Field(
        description='Никнейм',
        kw_only=True,
        examples=['Username'],
    )
    email: str = Field(
        description='Почта',
        kw_only=True,
        examples=['example@mail.com'],
    )
    login: str = Field(
        description='Логин',
        kw_only=True,
        examples=['login'],
    )
    password: str = Field(
        description='Пароль',
        kw_only=True,
        examples=['qwerty'],
    )
