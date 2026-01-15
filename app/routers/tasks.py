from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.task_schema import Task, TaskCreate
from app.crud.task import get_tasks, create_task, delete_task

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.post("/tasks", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return deleted_task
