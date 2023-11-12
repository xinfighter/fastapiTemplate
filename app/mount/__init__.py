from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from settings import settings


def mount_init(app: FastAPI):
    if settings.debug:
        directory = Path(__file__).parent.parent.parent / 'static'
        app.mount('/static', StaticFiles(directory=directory), name='static')
