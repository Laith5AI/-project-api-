from fastapi import FastAPI

app = FastAPI(
    title="Mini Project Management API",
    description="An API for managing projects and tasks",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to the Project Management API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.1.0", "name": "Mini PM API"}