from datetime import datetime

from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings

from .mixin_auto_id_model import MixinAutoIdModel
from .mixin_soft_delete_model import MixinSoftDeleteModel


class PostModel(MixinAutoIdModel, MixinSoftDeleteModel):
    """Модель постов."""

    __abstract__ = False
    __tablename__ = 'post'
    __table_args__ = {
        'schema': app_settings.POSTS_SQL_SCHEMA,
    }

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment='Название поста',
        sort_order=-50,
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment='Контент',
        sort_order=-40,
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(),
        nullable=False,
        server_default=text('NOW()'),
        comment='Создан',
        sort_order=-20,
    )
