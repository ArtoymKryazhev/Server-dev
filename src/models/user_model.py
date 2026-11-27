from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings

from .mixin_auto_id_model import MixinAutoIdModel
from .mixin_soft_delete_model import MixinSoftDeleteModel


class UserModel(MixinAutoIdModel, MixinSoftDeleteModel):
    """Модель пользователя."""

    __abstract__ = False
    __tablename__ = 'user'
    __table_args__ = {
        'schema': app_settings.USERS_SQL_SCHEMA,
    }

    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        comment='Никнейм пользователя',
        sort_order=-20,
    )
    email: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
        comment='Почта',
        sort_order=-15,
    )
    login: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        comment='Логин',
        sort_order=-10,
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment='Пароль',
        sort_order=-5,
    )
    last_login_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(),
        nullable=True,
        default=None,
        comment='Последний вход',
        sort_order=-1,
    )
