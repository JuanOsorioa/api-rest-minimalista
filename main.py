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

@app.delete("/tasks/{index}")
def eliminar_tarea(index: int):
    if index < len(tareas):
        tareas.pop(index)
        return {"mensaje": "Tarea eliminada"}
    return {"mensaje": "Tarea no encontrada"}