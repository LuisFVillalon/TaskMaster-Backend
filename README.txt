Object Schema:
    const TAG_COLORS = [
    "#ef4444", // red
    "#f97316", // orange
    "#eab308", // yellow
    "#22c55e", // green
    "#3b82f6", // blue
    "#6366f1", // indigo
    "#a855f7", // purple
    "#ec4899"  // pink
    ]
    Task {
        id: number
        title: string
        description: string | null
        completed: boolean
        urgent: boolean
        due_at: datetime | null
        tags: Tag[]

    }
    Tag {
        id: number
        name:string
        color: string | null
    }
Tools:
    FastAPI - API & routing
    Pydantic - Validation & serializaion 
    SQLAlchemy - Python <-> SQL Mapping
    psychopg2 - PostgreSQL communication
    Alembic - Schema versioning 

