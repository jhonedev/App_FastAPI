from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from api.api_v1.router import Router
from models.user_model import User
from models.task_model import Task

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.on_event('startup')
async def app_init():
    client_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    ).todoapp

    await init_beanie(
        database=client_db,
        document_models=[
            User,
            Task
        ]
    )

app.include_router(
    Router,
    prefix=settings.API_V1_STR
)