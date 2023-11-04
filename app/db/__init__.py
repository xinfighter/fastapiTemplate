from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import settings

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': settings.mysql_host,
                'port': settings.mysql_port,
                'user': settings.mysql_user,
                'password': settings.mysql_password,
                'database': settings.mysql_db_name,
                'minsize': 10,
                'maxsize': 50,
                'charset': 'utf8mb4'
            }
        }
    },
    "apps": {
        "models": {
            "default_connection": "default",
            "models": ["app.models", "aerich.models"]
        }
    },
    "use_tz": False,
    "timezone": settings.timezone,
}


def db_init(app: FastAPI):
    register_tortoise(app, config=TORTOISE_ORM)
