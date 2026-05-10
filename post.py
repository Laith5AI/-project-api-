from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    owner: str = Field(..., min_length=2)


@app.post("/projects")
def create_project(project: ProjectCreate):
    # FastAPI has already parsed and validated the request body for us.
    # Inside this function, `project` is a fully validated ProjectCreate object.
    return {
        "message": "Project created",
        "data": project,
    }