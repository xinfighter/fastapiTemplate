from fastapi import FastAPI

from app.apis import routers_init
from app.db import db_init
from app.middlewares import middleware_init
from app.events import events_init

app = FastAPI(
    title='Title',
    version='1.0.0',
    redoc_url=None,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

routers_init(app)
middleware_init(app)
db_init(app)
events_init(app)
