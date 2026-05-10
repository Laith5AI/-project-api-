# Mini Project Management API

A small REST API built with FastAPI for learning backend development. Manages projects and tasks, with full CRUD operations and a SQLite-backed database.

## Features

- Create, read, update, and delete projects
- Tasks nested within projects
- Filtering and pagination
- Auto-generated interactive documentation at `/docs`

## Requirements

- Python 3.10 or newer
- pip

## Installation

```bash
# Clone the repository
git clone git@github.com:yourusername/project-api.git
cd project-api

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the API

```bash
fastapi dev main.py
```

The server starts on `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` for the interactive documentation.

## Project Structure

```
project-api/
├── main.py             # entry point
├── database.py         # SQLAlchemy setup
├── models.py           # database models
├── schemas.py          # Pydantic models
├── routers/            # route definitions
│   ├── projects.py
│   └── tasks.py
└── requirements.txt
```

## Usage Examples

Create a project:

```bash
curl -X POST http://127.0.0.1:8000/projects \
  -H "Content-Type: application/json" \
  -d '{"title": "Build website", "owner": "laith"}'
```

List all projects:

```bash
curl http://127.0.0.1:8000/projects
```

## Author

Laith — learning backend development through deliberate practice.
