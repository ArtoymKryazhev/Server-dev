from typing import Annotated
from typing import Any
from typing import Dict

from fastapi import APIRouter
from fastapi import Depends

from src.controllers import AuthenticationController
from src.dependencies import get_authentication_controller
from src.schemas.requests import RefreshTokenRequest
from src.schemas.requests import VerifyAccessTokenRequest
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse

authentication_router = APIRouter(
    prefix='/authentication',
    tags=['Аутентификация'],
    deprecated=False,
    dependencies=None,
)


@authentication_router.post(path='/logout', summary='Выход пользователя')
async def logout(
        refresh_token_request: RefreshTokenRequest,
        authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> Dict[str, Any]:
    """Выход пользователя из приложения."""
    return await authentication_controller.logout_user(refresh_token_request=refresh_token_request)


@authentication_router.post(
    path='/verify_access_token',
    summary='Проверка access-токена',
    response_model=VerifyAccessTokenResponse,
)
async def verify_access_token(
        verify_access_token_request: VerifyAccessTokenRequest,
        authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> VerifyAccessTokenResponse:
    """Проверка access-токена."""
    return await authentication_controller.verify_access_token(
        verify_access_token_request=verify_access_token_request,
    )


@authentication_router.post(
    path='/refresh_tokens',
    summary='Обновление пары токенов',
    response_model=TokensResponse,
)
async def refresh_tokens(
        refresh_token_request: RefreshTokenRequest,
        authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> TokensResponse:
    """Обновление пары токенов."""
    return await authentication_controller.refresh_tokens(refresh_token_request=refresh_token_request)
