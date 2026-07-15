from fastapi import FastAPI

app = FastAPI(title="VAB-OS API")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "Тест", "done": False}]
