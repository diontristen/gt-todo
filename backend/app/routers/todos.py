import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models import Todo, TodoStatus
from app.schemas import TodoCreate, TodoResponse, TodoUpdate

router = APIRouter(prefix="/api/todos", tags=["todos"])

Session = Annotated[AsyncSession, Depends(get_session)]


@router.post("", response_model=TodoResponse, status_code=201)
async def create_todo(todo_in: TodoCreate, session: Session):
    todo = Todo(**todo_in.model_dump())
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo


@router.get("", response_model=list[TodoResponse])
async def list_todos(
    session: Session,
    status: TodoStatus | None = None,
    search: Annotated[str | None, Query(max_length=255)] = None,
):
    stmt = select(Todo)
    if status is not None:
        stmt = stmt.where(Todo.status == status)
    if search is not None:
        stmt = stmt.where(Todo.title.icontains(search))
    stmt = stmt.order_by(Todo.position, Todo.created_at)
    result = await session.execute(stmt)
    return result.scalars().all()


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: uuid.UUID, session: Session):
    todo = await session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: uuid.UUID, todo_in: TodoUpdate, session: Session):
    todo = await session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    update_data = todo_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    await session.commit()
    await session.refresh(todo)
    return todo


@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: uuid.UUID, session: Session):
    todo = await session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    await session.delete(todo)
    await session.commit()
