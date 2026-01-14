from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.schemas.tag import Tag


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    urgent: bool
    due_at: Optional[datetime] = None
    tags: List[Tag] = []
