from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.tag_schema import Tag, TagCreate
from app.crud.tag import get_tags, create_tag

router = APIRouter()

@router.get("/tags", response_model=list[Tag])
def read_tags(db: Session = Depends(get_db)):
    return get_tags(db)

@router.post("/tags", response_model=Tag)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)