from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate, TaskUpdate
from models.user_model import User
from api.depedencies.user_deps import get_current_user
from services.task_service import TaskService
from models.task_model import Task
from typing import List
from uuid import UUID

task_router = APIRouter()

@task_router.get('/', summary='Lista as tarefas', response_model=List[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(user)

@task_router.get('/{task_id}', summary='Detalhe de uma tarefa por ID', response_model=TaskDetail)
async def detail(task_id: UUID, user: User = Depends(get_current_user)):
    return await TaskService.detail(user, task_id)

@task_router.post('/create', summary='Adiciona tarefa', response_model=Task)
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(user, data)

@task_router.put('/{task_id}', summary='Atualiza tarefa', response_model=TaskDetail)
async def update(task_id: UUID, data: TaskUpdate, user: User = Depends(get_current_user)):
    return await TaskService.update_task(user, task_id, data)

@task_router.delete('/{tasl_id}', summary='Exclui tarefa')
async def delete(task_id: UUID, user: User = Depends(get_current_user)):
    await TaskService.delete_task(user, task_id)
    return None