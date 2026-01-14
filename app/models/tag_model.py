from sqlalchemy import Column, Integer, String
from app.db.database import Base
from sqlalchemy.orm import relationship
from app.models.association_tables import task_tags

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    color = Column(String)
    tasks = relationship(
        "Task",
        secondary=task_tags,
        back_populates="tags"
    )