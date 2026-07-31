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