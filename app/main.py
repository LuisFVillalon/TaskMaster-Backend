from fastapi import FastAPI
from datetime import datetime
from app.schemas.task import Task, Tag

app = FastAPI()


@app.get("/", response_model=Task)
async def root():
    return Task(
        id=1,
        title="Finish CS homework",
        description="Chapter 5 problems",
        completed=False,
        urgent=True,
        due_at=datetime(2026, 1, 20, 23, 59),
        tags=[
            Tag(id=1, name="school", color="#3b82f6"),
            Tag(id=2, name="hewalth", color="#ef4444")
        ]
    )
