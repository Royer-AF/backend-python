from fastapi import FastAPI

# Inicializamos la aplicación
app = FastAPI()

# Definimos una ruta (Endpoint) tipo GET
@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi primera API Web con Python!"}

@app.get("/curso")
def obtener_curso():
    return {
        "curso": "Python Backend",
        "nivel": "Intermedio",
        "estado": "Activo"
    }
