from datetime import date, time
from typing import List, Optional
from pydantic import BaseModel, field_validator
from app.schemas.tag_schema import Tag


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    urgent: bool = False

    due_date: Optional[date] = None
    due_time: Optional[time] = None

    tags: List[Tag] = []

    @field_validator("due_date", "due_time", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    model_config = {
        "from_attributes": True
    }
