from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class AccessTokenFullDto(MixinIdSchema):
    """DTO access-токена."""

    user_id: int = Field(
        description='ID пользователя',
        ge=0,
        kw_only=True,
    )
    expire_at: datetime = Field(
        description='Срок действия токена',
        kw_only=True,
    )
    created_at: datetime = Field(
        description='Время создания токена',
        kw_only=True,
    )
    refresh_id: int = Field(
        ge=1,
        description='ID refresh-токена',
        kw_only=True,
    )
