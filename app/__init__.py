from fastapi import FastAPI

from app.apis import routers_init
from app.db import db_init
from app.middlewares import middleware_init
from app.events import events_init
from app.mount import mount_init


def create_app():
    app = FastAPI(
        title='Title',
        version='1.0.0',
        docs_url=None,
        redoc_url=None
    )

    routers_init(app)
    middleware_init(app)
    db_init(app)
    events_init(app)
    mount_init(app)

    return app
