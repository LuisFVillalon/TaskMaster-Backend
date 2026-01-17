from sqlalchemy.orm import Session
from app.models.tag_model import Tag as TagModel
from app.schemas.tag_schema import TagCreate


def get_tags(db: Session):
    return db.query(TagModel).all()

def create_tag(db: Session, tag: TagCreate):
    db_tag = TagModel(name=tag.name, color=tag.color)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    tag = db.query(TagModel).filter(TagModel.id == tag_id).first()

    if not tag:
        return None

    db.delete(tag)
    db.commit()
    return tag    

def update_tag(db: Session, tag_id: int, tag: TagCreate):
    # 1. Get existing task
    db_tag = db.query(TagModel).filter(TagModel.id == tag_id).first()

    if not db_tag:
        return None  # or raise HTTPException(404)

    # 2. Update scalar fields
    db_tag.name = tag.name
    db_tag.color = tag.color

    # 5. Commit & refresh the DB model
    db.commit()
    db.refresh(db_tag)

    return db_tag
