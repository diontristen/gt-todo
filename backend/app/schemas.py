import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models import TodoStatus


class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    status: TodoStatus = TodoStatus.todo
    position: int = 0


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TodoStatus | None = None
    position: int | None = None


class TodoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str | None
    status: TodoStatus
    position: int
    created_at: datetime
    updated_at: datetime
