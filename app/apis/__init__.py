from fastapi import FastAPI

from .token import token_router
from .user import user_router


def routers_init(app: FastAPI):
    app.include_router(token_router)
    app.include_router(user_router)
