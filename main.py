from fastapi import FastAPI
from uvicorn import run

from src.routers import post_router
from src.routers import user_router

app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)


def main():
    """Запуск сервера."""
    run(
        app,
        host='127.0.0.1',
        port=8000,
    )


if __name__ == '__main__':
    main()
