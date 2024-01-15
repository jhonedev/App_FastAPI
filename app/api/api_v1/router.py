from fastapi import APIRouter
from api.api_v1.handlers import user, task
from api.auth.jwt import auth_router

Router = APIRouter()

Router.include_router(
    user.user_router,
    prefix='/users',
    tags=['users']
)

Router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

Router.include_router(
    task.task_router,
    prefix='/task',
    tags=['task']
)