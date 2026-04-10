"""
Work Blocks — REST endpoints for the Smart Scheduling feature.

Lifecycle
─────────
  POST   /work-blocks           AI service creates a 'suggested' block
  GET    /work-blocks           Frontend fetches all non-dismissed blocks for calendar render
  PATCH  /work-blocks/{id}      User confirms ('confirmed') or dismisses ('dismissed') a block
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import UserInfo, get_current_user
from app.crud.work_block_crud import (
    create_work_block,
    get_work_blocks_for_user,
    update_work_block_status,
)
from app.database.database import get_db
from app.schemas.work_block_schema import WorkBlockCreate, WorkBlockOut, WorkBlockUpdate

router = APIRouter(prefix="/work-blocks", tags=["work-blocks"])


@router.post("", response_model=WorkBlockOut, status_code=status.HTTP_201_CREATED)
def create_block(
    data: WorkBlockCreate,
    current_user: UserInfo = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Called by the AI service after it has selected the best slot.
    The JWT is forwarded from the frontend, so user isolation is enforced
    by the same auth middleware used by every other endpoint.
    """
    return create_work_block(db, data, current_user.id)


@router.get("", response_model=list[WorkBlockOut])
def list_blocks(
    current_user: UserInfo = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Return all suggested and confirmed work blocks for the current user.
    The calendar view calls this alongside /google-calendar/events to
    render both external events and AI-scheduled work sessions.
    """
    return get_work_blocks_for_user(db, current_user.id)


@router.patch("/{block_id}", response_model=WorkBlockOut)
def update_block(
    block_id: int,
    data: WorkBlockUpdate,
    current_user: UserInfo = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Accept ('confirmed') or dismiss ('dismissed') a suggested work block.
    Only blocks owned by the authenticated user can be modified.
    """
    block = update_work_block_status(db, block_id, current_user.id, data.status)
    if not block:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Work block not found",
        )
    return block
