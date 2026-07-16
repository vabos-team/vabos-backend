from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = 1

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: int = 1
    done: bool = False

db: list[Task] = []
next_id = 1

app = FastAPI(title="VAB-OS API")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "Тест", "done": False}]

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, title=task.title, description=task.description, priority=task.priority)
    db.append(new_task)
    next_id += 1
    return new_task
