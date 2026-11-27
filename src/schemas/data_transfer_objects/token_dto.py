from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class TokenDto(MixinIdSchema):
    """DTO токена."""

    user_id: int = Field(
        ge=1,
        description='Идентификатор пользователя',
        kw_only=True,
    )
    expire_at: datetime = Field(
        description='Срок действия токена',
        kw_only=True,
        examples=[datetime.now()],
    )
    created_at: datetime = Field(
        description='Дата и время создания токена',
        kw_only=True,
        examples=[datetime.now()],
    )
