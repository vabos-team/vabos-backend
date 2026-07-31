from fastapi import APIRouter, HTTPException
from schemas.tasks import Task, TaskCreate

# Создаем роутер с префиксом /tasks

router = APIRouter(prefix="/tasks", tags=["Задачи"])

db: list[Task] = []
next_id = 1

@router.get("/", response_model=list[Task])
def get_tasks():
    return db

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, title=task.title, description=task.description, priority=task.priority)
    db.append(new_task)
    next_id += 1
    return new_task
    

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated: TaskCreate):
    for task in db:
        if task.id == task_id:
            task.title = updated.title
            task.description = updated.description
            task.priority = updated.priority
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(db):
        if task.id == task_id:
            db.pop(i)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")