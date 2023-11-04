from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from app.models import User
from settings import settings

token_router = APIRouter(prefix='/api/v1/token', tags=['Token'])


@token_router.post('/')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=data.username)
    if not (user and user.verify_password(data.password)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='用户名或密码错误',
                            headers={"WWW-Authenticate": "Bearer"}, )
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=settings.EXPIRE)
    }
    access_token = jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)
    return {'access_token': access_token, 'token_type': 'bearer'}
