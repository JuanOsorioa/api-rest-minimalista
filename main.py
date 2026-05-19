from fastapi import FastAPI

app = FastAPI()

tareas = []

@app.get("/tasks")
def obtener_tareas():
    return tareas

@app.post("/tasks")
def crear_tarea(tarea: str):
    tareas.append(tarea)
    return {"mensaje": "Tarea creada"}