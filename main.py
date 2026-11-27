from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from uvicorn import run

from src.exceptions import BaseResponseError
from src.routers import authentication_router
from src.routers import authorization_router
from src.routers import post_router
from src.routers import user_router

app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)
app.include_router(authorization_router)
app.include_router(authentication_router)


@app.exception_handler(BaseResponseError)
async def handle_response_error(request: Request, exc: BaseResponseError) -> JSONResponse:
    """Ответ с кодом и текстом прикладной ошибки."""
    return JSONResponse(status_code=exc.code, content={'detail': exc.message})


def main():
    """Запуск сервера."""
    run(
        app,
        host='127.0.0.1',
        port=8000,
    )


if __name__ == '__main__':
    main()
