import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de Pydantic para validar los datos que entran
class ProductoNuevo(BaseModel):
    id: int
    nombre: str
    precio: float

# Funciones de lectura y escritura en archivo
def cargar_datos():
    try:
        with open("productos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

# Endpoints de la API
@app.get("/productos/{producto_id}")
def buscar_producto(producto_id: int):
    catalogo = cargar_datos()
    for prod in catalogo:
        if prod["id"] == producto_id:
            return prod
    return {"error": "Producto no encontrado"}

@app.post("/productos")
def crear_producto(producto: ProductoNuevo):
    catalogo = cargar_datos()
    nuevo_dict = producto.model_dump()

    catalogo.append(nuevo_dict)
    guardar_datos(catalogo) # Guarda físicamente en el archivo

    return {"mensaje": "Producto creado y guardado con éxito", "producto": nuevo_dict}
