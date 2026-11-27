from src.enums import MessageEnum

from .base_custom_error import BaseCustomError


class BaseResponseError(BaseCustomError):
    """Базовый класс ошибок ответов."""

    def __init__(self, message: MessageEnum, code: int):
        super().__init__(message=message.value)
        self._code = code

    @property
    def code(self) -> int:
        return self._code
