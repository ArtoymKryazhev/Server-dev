from datetime import datetime
from typing import Optional

from pydantic import Field

from src.schemas.common import MixinIdSchema
from src.schemas.common import MixinSoftDeleteSchema


class PostFullDto(MixinIdSchema, MixinSoftDeleteSchema):
    """Полный DTO постов."""

    name: str = Field(
        description='Название поста',
        kw_only=True,
        examples=['Название'],
    )
    content: str = Field(
        description='Контент',
        kw_only=True,
        examples=['Текст поста'],
    )
    created_at: Optional[datetime] = Field(
        description='Создан',
        default=None,
        kw_only=True,
    )
