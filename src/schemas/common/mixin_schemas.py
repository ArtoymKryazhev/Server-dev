from datetime import datetime
from typing import Optional

from pydantic import Field

from .base_schema import BaseSchema


class MixinIdSchema(BaseSchema):
    """Поле идентификатора."""

    id: Optional[int] = Field(
        description='Идентификатор',
        default=None,
        ge=1,
        kw_only=True,
        examples=[1],
    )


class MixinSoftDeleteSchema(BaseSchema):
    """Поля мягкого удаления."""

    is_deleted: bool = Field(
        description='Удалено',
        default=False,
        kw_only=True,
    )
    deleted_by: Optional[int] = Field(
        description='Удалил',
        default=None,
        kw_only=True,
    )
    deleted_at: Optional[datetime] = Field(
        description='Время удаления',
        default=None,
        kw_only=True,
    )
