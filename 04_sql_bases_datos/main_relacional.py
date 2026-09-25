from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

# Importamos nuestro motor y modelos de los archivos que acabas de crear
from database import crear_db_y_tablas, get_session
from models import Categoria, ProductoRel

app = FastAPI(title="API Relacional con SQLModel")

@app.on_event("startup")
def on_startup():
    crear_db_y_tablas()

# --- ENDPOINTS PARA CATEGORÍAS ---

@app.post("/categorias", response_model=Categoria)
def crear_categoria(categoria: Categoria, session: Session = Depends(get_session)):
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

@app.get("/categorias", response_model=List[Categoria])
def listar_categorias(session: Session = Depends(get_session)):
    categorias = session.exec(select(Categoria)).all()
    return categorias

# --- ENDPOINTS PARA PRODUCTOS CON CATEGORÍA ---

@app.post("/productos", response_model=ProductoRel)
def crear_producto(producto: ProductoRel, session: Session = Depends(get_session)):
    # Validar si la categoría asignada existe en la BD
    if producto.categoria_id:
        categoria = session.get(Categoria, producto.categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="La categoría especificada no existe")
            
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

@app.get("/categorias/{categoria_id}/productos", response_model=List[ProductoRel])
def obtener_productos_por_categoria(categoria_id: int, session: Session = Depends(get_session)):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria.productos