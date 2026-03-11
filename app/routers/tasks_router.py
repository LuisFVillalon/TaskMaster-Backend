from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.config.supabase_client import supabase
from app.database.database import get_db
from app.schemas.task_schema import Task, TaskCreate
from app.crud.task_crud import get_tasks, create_task, delete_task, update_task_status, update_task

router = APIRouter()

@router.get("/get-tasks", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.post("/create-task", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.delete("/del-task/{task_id}", response_model=Task)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return deleted_task

@router.patch("/update-task-status/{task_id}", response_model=Task)
def update_complete_status_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = update_task_status(db, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task

@router.put("/update-task/{task_id}", response_model=Task)
def update_task_by_id(
    task_id: int,
    payload: TaskCreate,
    db: Session = Depends(get_db)
):
    task = update_task(db, task_id, payload)


    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task

@router.post("/save-tasks-list")
async def create_new_tasks(tasks: List[TaskCreate]):

    created_tasks = []

    for task in tasks:
        task_data = task.model_dump(mode="json")

        # Extract tags
        tags = task_data.pop("tags", [])

        # Insert task
        task_response = supabase.table("tasks").insert(task_data).execute()

        if not task_response.data:
            raise HTTPException(status_code=400, detail="Task insert failed")

        inserted_task = task_response.data[0]
        task_id = inserted_task["id"]

        # Insert into task_tags table
        if tags:
            tag_rows = [
                {"task_id": task_id, "tag_id": tag["id"]}
                for tag in tags
            ]
            supabase.table("task_tags").insert(tag_rows).execute()

        created_tasks.append(inserted_task)

    return created_tasks