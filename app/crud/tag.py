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