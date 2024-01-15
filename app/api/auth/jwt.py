from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import creat_acess_token, creat_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from models.user_model import User
from api.depedencies.user_deps import get_current_user

auth_router = APIRouter()

@auth_router.post(
        '/login',
        summary='Cria Acess Token e Refresh Token',
        response_model=TokenSchema
)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email = data.username,
        password = data.password
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail ou senha estão incorretos.'
        )
    
    return {
        'access_token': creat_acess_token(usuario.user_id),
        'refresh_token': creat_refresh_token(usuario.user_id)
    }

@auth_router.post(
    '/test-token',
    summary='Testando o Token',
    response_model=UserDetail
)
async def test_token(user: User = Depends(get_current_user)):
    return user