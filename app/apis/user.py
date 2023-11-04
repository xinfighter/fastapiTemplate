from fastapi import APIRouter, Depends, HTTPException, Query, status
from tortoise.exceptions import IntegrityError

from app.models import User
from app.dependencies import token_verify
from app.schemas import UserOut, UserListOut, UserCreate, UserUpdate
from app.utils import crypt

user_router = APIRouter(prefix='/api/v1/user', tags=['User'], dependencies=[Depends(token_verify)])


@user_router.get('/', response_model=UserListOut)
async def get_users(page: int = Query(1, ge=1), size: int = Query(100, ge=1)):
    items = await User.all().offset((page - 1) * size).limit(size)
    return {'total': len(items), 'count': len(items), 'items': items}


@user_router.get('/{user_id}/', response_model=UserOut)
async def get_user(user_id: int):
    try:
        return await User.get(pk=user_id)
    except:
        raise HTTPException(status_code=404, detail='User not found')


@user_router.post('/', response_model=UserOut)
async def create_user(data: UserCreate):
    data.password = crypt.hash(data.password)
    try:
        return await User.create(**data.model_dump(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='username has used')


@user_router.put('/{user_id}', response_model=UserOut)
async def update_user(user_id: int, data: UserUpdate):
    await User.filter(pk=user_id).update(**data.model_dump(exclude_unset=True))
    return await User.get(pk=user_id)


@user_router.delete('/{user_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    delete_count = await User.filter(pk=user_id).delete()
    if not delete_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
