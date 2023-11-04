from fastapi import FastAPI

from app.utils import crypt
from app.models import User


def events_init(app: FastAPI):
    """
    注册fastapi事件方法
    """
    app.add_event_handler('startup', _init_data)


async def _init_data():
    """
    创建初始数据
    """
    password = crypt.hash('admin')
    await User.get_or_create(pk=1, defaults={'username': 'admin', 'password': password})
