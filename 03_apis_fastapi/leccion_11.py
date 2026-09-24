from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI


class ProductoNuevo(BaseModel):
    id: int
    nombre: str
    precio: float

catalogo = [
    {"id": 1, "nombre": "Laptop Lenovo", "precio": 2500.0}
]

@app.post("/productos")
def crear_producto(producto: ProductoNuevo):
    nuevo_dict = producto.model_dump()

    catalogo.append(nuevo_dict)

    return {"mensaje": "Producto creado con éxito", "producto": nuevo_dict}