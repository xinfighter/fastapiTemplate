from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt

from settings import settings

auth_depend = OAuth2PasswordBearer(tokenUrl='api/v1/token/')


async def token_verify(token: Annotated[str, Depends(auth_depend)]):
    """
    token验证依赖
    :param token: str JWT Token
    :return: payload or Error
    """
    try:
        return jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
