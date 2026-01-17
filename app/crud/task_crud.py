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

def update_complete_task(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        return None

    # Toggle complete status
    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task

def update_task_status(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        return None

    # Toggle complete status
    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task    

def update_task(db: Session, task_id: int, task: TaskCreate):
    # 1. Get existing task
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not db_task:
        return None  # or raise HTTPException(404)

    # 2. Update scalar fields
    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db_task.urgent = task.urgent
    db_task.due_date = task.due_date
    db_task.due_time = task.due_time

    # 3. Clear existing tags
    db_task.tags.clear()

    # 4. Re-attach tags
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
            db.flush()  # ensures tag.id exists

        db_task.tags.append(tag)

    # 5. Commit & refresh the DB model
    db.commit()
    db.refresh(db_task)

    return db_task


