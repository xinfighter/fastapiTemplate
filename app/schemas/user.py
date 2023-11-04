from datetime import datetime
from pydantic import BaseModel
from fastapi import Body

from app.utils import datetime_format


class UserOut(BaseModel):
    id: int
    username: str = ''
    age: int = 1
    created: datetime
    updated: datetime

    class Config:
        json_encoders = {
            datetime: datetime_format
        }


class UserListOut(BaseModel):
    total: int = 0
    count: int = 0
    items: list[UserOut] = []


class UserCreate(BaseModel):
    username: str = Body(min_length=1, max_length=20)
    password: str = Body(pattern=r'^[a-zA-Z0-9]{8,16}$')
    age: int | None = 0


class UserUpdate(BaseModel):
    username: str | None = Body(default=None, min_length=1, max_length=20)
    age: int = 0
