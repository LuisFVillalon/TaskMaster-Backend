from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.database.database import engine, Base
from app.routers import tags_router, tasks_router, canvas_router
from fastapi.middleware.cors import CORSMiddleware
import time
import psycopg2
from dotenv import load_dotenv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://task-master-mvp.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def startup():
    print("DATABASE_URL =", os.getenv("DATABASE_URL"))

app.include_router(tags_router.router)
app.include_router(tasks_router.router)
app.include_router(canvas_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMaster Backend"}