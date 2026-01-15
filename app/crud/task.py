from sqlalchemy.orm import Session
from app.models.tag_model import Tag as TagModel
from app.models.task_model import Task as TaskModel
from app.schemas.task_schema import TaskCreate


def get_tasks(db: Session):
    return db.query(TaskModel).all()

def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(
        title=task.title,
        description=task.description,
        completed=task.completed,
        urgent=task.urgent,
        due_date=task.due_date,
        due_time=task.due_time
    )
    for tag_data in task.tags:
        tag = (
            db.query(TagModel)
            .filter(TagModel.name == tag_data.name)
            .first()
        )
        if not tag:
            tag = TagModel(
                name=tag_data.name,
                color=tag_data.color
            )
            db.add(tag)
        db_task.tags.append(tag)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task
