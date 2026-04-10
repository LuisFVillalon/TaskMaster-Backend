from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func

from app.database.database import Base


class WorkBlock(Base):
    __tablename__ = "work_blocks"

    id           = Column(Integer, primary_key=True, index=True)
    task_id      = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id      = Column(String(36), nullable=False, index=True)
    start_time   = Column(TIMESTAMP(timezone=True), nullable=False)
    end_time     = Column(TIMESTAMP(timezone=True), nullable=False)
    # 'suggested' | 'confirmed' | 'dismissed'
    status       = Column(String(20), nullable=False, default="suggested")
    ai_reasoning = Column(Text, nullable=True)
    confidence   = Column(Float, nullable=True)
    created_at   = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
