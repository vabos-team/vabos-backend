from fastapi import FastAPI, HTTPException
from schemas.tasks import Task, TaskCreate
from routers import tasks


app = FastAPI(title="VAB-OS API")

@app.get("/health")
def health():
    return {"status": "OK"}

app.include_router(tasks.router)