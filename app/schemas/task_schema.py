from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., title='Título', min_length=3, max_length=50)
    description: str = Field(..., title='Descrição', min_length=3, max_length=150)
    status: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = False

class TaskDetail(BaseModel):
    task_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updadet_at: datetime