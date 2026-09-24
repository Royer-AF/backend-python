from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "¡Servidor FastAPI corriendo exitosamente en Linux Mint!"}

@app.get("/producto")
def obtener_producto():
    return {
        "nombre": "Curso Python Pro",
        "precio": 49.90,
        "link_descarga": "https://upc.edu.pe/curso",
        "disponible": True
    }