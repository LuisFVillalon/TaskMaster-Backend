from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError


from app.db.database import engine, Base
from app.routers import tags_router, tasks_router
from fastapi.middleware.cors import CORSMiddleware

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
    for _ in range(5):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected")
            return
        except OperationalError as e:
            print("⏳ Waiting for database...")
            time.sleep(2)
    raise RuntimeError("❌ Database unavailable")

app.include_router(tags_router.router)
app.include_router(tasks_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMaster Backend"}