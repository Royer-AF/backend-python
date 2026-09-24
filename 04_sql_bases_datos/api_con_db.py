from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

# --- 1. MODELOS DE DATOS ---


class ProductoBase(SQLModel):
    nombre: str
    precio: float

# Modelo de la Tabla (Base de Datos)


class Producto(ProductoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# Modelo para recibir datos por POST (sin ID)


class ProductoCrear(ProductoBase):
    pass


# --- 2. CONFIGURACIÓN DE BASE DE DATOS ---
sqlite_file_name = "04_sql_bases_datos/tienda_api.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)


def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)

# Evento de inicio de la API: crea las tablas automáticamente al encender


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_db_y_tablas()
    yield

app = FastAPI(lifespan=lifespan)

# --- 3. ENDPOINTS DE LA API ---

# POST: Crear un nuevo producto en la BD


@app.post("/productos", response_model=Producto)
def crear_producto(producto: ProductoCrear):
    with Session(engine) as session:
        # Convertimos el modelo de entrada al modelo de tabla
        db_producto = Producto.model_validate(producto)
        session.add(db_producto)
        session.commit()
        session.refresh(db_producto)
        return db_producto

# GET: Obtener TODOS los productos de la BD


@app.get("/productos", response_model=List[Producto])
def listar_productos():
    with Session(engine) as session:
        productos = session.exec(select(Producto)).all()
        return productos

# GET: Buscar un producto por ID


@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    with Session(engine) as session:
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(
                status_code=404, detail="Producto no encontrado")
        return producto


# PUT: Actualizar un producto existente
@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, producto_datos: ProductoCrear):
    with Session(engine) as session:
        db_producto = session.get(Producto, producto_id)
        if not db_producto:
            raise HTTPException(
                status_code=404, detail="Producto no encontrado")

        # Sobrescribimos los campos del objeto en la BD con los datos recibidos
        datos_nuevos = producto_datos.model_dump(exclude_unset=True)
        db_producto.sqlmodel_update(datos_nuevos)

        session.add(db_producto)
        session.commit()
        session.refresh(db_producto)
        return db_producto

# DELETE: Eliminar un producto


@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    with Session(engine) as session:
        db_producto = session.get(Producto, producto_id)
        if not db_producto:
            raise HTTPException(
                status_code=404, detail="Producto no encontrado")

        session.delete(db_producto)
        session.commit()
        return {"mensaje": f"Producto con ID {producto_id} eliminado exitosamente"}
