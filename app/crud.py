from sqlalchemy.orm import Session
from app.models.tag_model import Tag as TagModel
from app.models.task_model import Task as TaskModel
from app.schemas.tag_schema import TagCreate
from app.schemas.task_schema import TaskCreate


def get_tags(db: Session):
    return db.query(TagModel).all()


def create_tag(db: Session, tag: TagCreate):
    db_tag = TagModel(name=tag.name, color=tag.color)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tasks(db: Session):
    return db.query(TaskModel).all()

def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(title=task.title, 
        description = task.description, 
        completed = task.completed, 
        urgent = task.urgent, 
        due_at = task.due_at, 
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task