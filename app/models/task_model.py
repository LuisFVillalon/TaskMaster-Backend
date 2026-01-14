from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.association_tables import task_tags

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    urgent = Column(Boolean, default=False)
    due_at = Column(DateTime)

    tags = relationship(
        "Tag",
        secondary=task_tags,
        back_populates="tasks"
    )
