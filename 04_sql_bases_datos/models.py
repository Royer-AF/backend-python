from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

# --- TABLA CATEGORÍA ---
class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    
    # Relación inversa: Una categoría tiene MUCHOS productos
    productos: List["ProductoRel"] = Relationship(back_populates="categoria")

# --- TABLA PRODUCTO (CON RELACIÓN) ---
class ProductoRel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    
    # Clave Foránea (Foreign Key) vinculada a la tabla categoria
    categoria_id: Optional[int] = Field(default=None, foreign_key="categoria.id")
    
    # Relación principal: Un producto pertenece a UNA categoría
    categoria: Optional[Categoria] = Relationship(back_populates="productos")