from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


_VALID_STATUSES = {"suggested", "confirmed", "dismissed"}


class WorkBlockCreate(BaseModel):
    task_id:      int
    start_time:   datetime
    end_time:     datetime
    ai_reasoning: Optional[str]   = None
    confidence:   Optional[float] = None
    # AI service always sends 'suggested'; frontend PATCH changes it later.
    status:       str             = "suggested"

    @field_validator("status")
    @classmethod
    def status_must_be_valid(cls, v: str) -> str:
        if v not in _VALID_STATUSES:
            raise ValueError(f"status must be one of {_VALID_STATUSES}")
        return v

    @field_validator("end_time")
    @classmethod
    def end_after_start(cls, v: datetime, info) -> datetime:
        start = info.data.get("start_time")
        if start and v <= start:
            raise ValueError("end_time must be after start_time")
        return v


class WorkBlockUpdate(BaseModel):
    status: str

    @field_validator("status")
    @classmethod
    def status_must_be_valid(cls, v: str) -> str:
        # Only the user-facing transitions are allowed here.
        allowed = {"confirmed", "dismissed"}
        if v not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        return v


class WorkBlockOut(BaseModel):
    id:           int
    task_id:      int
    user_id:      str
    start_time:   datetime
    end_time:     datetime
    status:       str
    ai_reasoning: Optional[str]
    confidence:   Optional[float]
    created_at:   datetime

    model_config = {"from_attributes": True}
