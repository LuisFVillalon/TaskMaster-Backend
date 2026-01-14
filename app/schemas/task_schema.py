from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.schemas.tag_schema import Tag


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    urgent: bool = False
    due_at: Optional[datetime] = None

class TaskCreate(TaskBase):
    tag_ids: List[int] = []

class Task(TaskBase):
    id: int
    tags: List[Tag] = []

    class Config:
        from_attributes = True
