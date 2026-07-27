from fastapi import FastAPI, HTTPException
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

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return db

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, title=task.title, description=task.description, priority=task.priority)
    db.append(new_task)
    next_id += 1
    return new_task
    

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: TaskCreate):
    for task in db:
        if task.id == task_id:
            task.title = updated.title
            task.description = updated.description
            task.priority = updated.priority
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(db):
        if task.id == task_id:
            db.pop(i)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")