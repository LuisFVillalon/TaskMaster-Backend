from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.db.database import engine, Base
from app.routers import tags_router, tasks_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",  # Next.js dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tags_router.router)
app.include_router(tasks_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMaster Backend"}