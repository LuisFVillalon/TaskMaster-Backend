from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, get_db, Base
from app.schemas.tag_schema import Tag, TagCreate
from app.schemas.task_schema import Task, TaskCreate
from app.crud import create_tag, get_tags, get_tasks, create_task

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMaster Backend"}


@app.get("/tags", response_model=list[Tag])
def read_tags(db: Session = Depends(get_db)):
    return get_tags(db)

@app.get("/tasks", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@app.post("/tags", response_model=Tag)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@app.post("/tasks", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)