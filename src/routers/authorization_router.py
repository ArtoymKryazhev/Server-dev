from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.controllers import AuthorizationController
from src.dependencies import get_authorization_controller
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse

authorization_router = APIRouter(
    prefix='/authorization',
    tags=['Авторизация'],
    deprecated=False,
    dependencies=None,
)


@authorization_router.post(
    path='/login',
    summary='Вход пользователя',
    response_model=TokensResponse,
)
async def user_login(
        login_request: LoginRequestSchema,
        authorization_controller: Annotated[AuthorizationController, Depends(get_authorization_controller)],
) -> TokensResponse:
    """Вход пользователя в приложение."""
    return await authorization_controller.login_user(login_request=login_request)
