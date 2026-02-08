from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.tag_schema import Tag, TagCreate
from app.crud.tag_crud import get_tags, create_tag, delete_tag, update_tag

router = APIRouter()

@router.get("/get-tags", response_model=list[Tag])
def read_tags(db: Session = Depends(get_db)):
    return get_tags(db)

@router.post("/create-tags", response_model=Tag)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@router.delete("/del-tag/{tag_id}", response_model=Tag)
def delete_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    deleted_tag = delete_tag(db, tag_id)

    if not deleted_tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found"
        )

    return deleted_tag

@router.put("/update-tag/{tag_id}", response_model=Tag)
def update_tag_by_id(
    tag_id: int,
    payload: TagCreate,
    db: Session = Depends(get_db)
):
    tag = update_tag(db, tag_id, payload)


    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="tag not found"
        )

    return tag