from typing import Union

from jose import jwt
from jose.exceptions import ExpiredSignatureError
from jose.exceptions import JWTError
from passlib.context import CryptContext

from settings import app_settings
from src.exceptions import ExpiredJwtTokenError
from src.exceptions import InvalidTokenError
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.data_transfer_objects import TokenDto

from .token_dto_mapper import TokenDtoMapper


class CommonUtils:
    """Базовые утилиты."""

    @staticmethod
    def create_jwt_token(token_dto: Union[AccessTokenFullDto, RefreshTokenFullDto]) -> str:
        """Создание JWT токена.

        :param token_dto: Сущность токена.
        :return: Токен.
        """
        token_dict = {
            'user': str(token_dto.user_id),
            'exp': token_dto.expire_at.timestamp(),
            'iat': token_dto.created_at.timestamp(),
            'jti': str(token_dto.id),
        }
        return str(jwt.encode(token_dict, app_settings.SECRET_KEY, algorithm=app_settings.JWT_ALGORITHM))

    @staticmethod
    def decode_jwt_token(token: str) -> TokenDto:
        """Декодирование JWT токена.

        :param token: Токен.
        :return: Данные токена.
        :raise ExpiredJwtTokenError: Если срок действия токена истек.
        :raise InvalidTokenError: Если токен невалидный.
        """
        try:
            decoded_dict = jwt.decode(
                token=token,
                key=app_settings.SECRET_KEY,
                algorithms=[app_settings.JWT_ALGORITHM],
            )
        except ExpiredSignatureError:
            raise ExpiredJwtTokenError()
        except JWTError:
            raise InvalidTokenError()
        return TokenDtoMapper.get_from_decoded_dict(decoded_dict=decoded_dict)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str, password_context: CryptContext) -> bool:
        """Проверка пароля.

        :param plain_password: Незашифрованный пароль.
        :param hashed_password: Зашифрованный пароль.
        :param password_context: Контекст хэширования.
        :return: Результат проверки пароля.
        """
        return bool(password_context.verify(plain_password, hashed_password))
