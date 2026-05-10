from fastapi import FastAPI, Path, Query, status
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(
    title="Mini Project Management API",
    description="Managing projects, learning FastAPI from the ground up.",
    version="0.1.0",
)


class ProjectStatus(str, Enum):
    active = "active"
    archived = "archived"
    completed = "completed"


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    owner: str = Field(..., min_length=2, max_length=50)
    status: ProjectStatus = ProjectStatus.active


class ProjectPublic(BaseModel):
    id: int
    title: str
    description: str
    owner: str
    status: ProjectStatus


fake_db: list[dict] = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Welcome to the Project Management API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post(
    "/projects",
    response_model=ProjectPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_project(project: ProjectCreate):
    global next_id
    new_project = project.model_dump()
    new_project["id"] = next_id
    next_id += 1
    fake_db.append(new_project)
    return new_project


@app.get("/projects", response_model=list[ProjectPublic])
def list_projects(
    status: ProjectStatus | None = None,
    owner: str | None = Query(default=None, min_length=2, max_length=50),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    results = fake_db
    if status is not None:
        results = [p for p in results if p["status"] == status]
    if owner is not None:
        results = [p for p in results if p["owner"] == owner]
    return results[offset : offset + limit]


@app.get("/projects/{project_id}", response_model=ProjectPublic)
def get_project(project_id: int = Path(..., gt=0)):
    for project in fake_db:
        if project["id"] == project_id:
            return project
    # We'll handle 404 properly in topic 8 — for now, this returns None
    # which won't match the response model, causing an error
    return None