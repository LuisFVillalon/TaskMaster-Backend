from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.task_tag_model import task_tags

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    urgent = Column(Boolean, default=False)
    due_date = Column(DateTime, nullable=True)
    due_time = Column(Time, nullable=True)
    tags = relationship(
        "Tag",
        secondary=task_tags,
        back_populates="tasks"
    )
