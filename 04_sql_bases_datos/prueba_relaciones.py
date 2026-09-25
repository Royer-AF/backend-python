from database import crear_db_y_tablas, engine
from models import Categoria, ProductoRel
from sqlmodel import Session, select

def ejecutar_prueba():
    crear_db_y_tablas()
    
    with Session(engine) as session:
        # 1. Crear una Categoria
        cat_tech = Categoria(nombre="Tecnología")
        
        # 2. Crear Productos asociados a esa categoría
        p1 = ProductoRel(nombre="Laptop Gamer", precio=3500.0, categoria=cat_tech)
        p2 = ProductoRel(nombre="Mouse Inalámbrico", precio=80.0, categoria=cat_tech)
        
        session.add(cat_tech)
        session.add(p1)
        session.add(p2)
        session.commit()
        
        print("--- REGISTROS CREADOS CON ÉXITO ---")

def consultar_relaciones():
    with Session(engine) as session:
        # Consultar la categoría y ver automáticamente sus productos asociados
        statement = select(Categoria).where(Categoria.nombre == "Tecnología")
        categoria = session.exec(statement).first()
        
        if categoria:
            print(f"\nCategoría: {categoria.nombre}")
            print("Productos pertenecientes a esta categoría:")
            for prod in categoria.productos:
                print(f" - {prod.nombre}: S/ {prod.precio}")

if __name__ == "__main__":
    ejecutar_prueba()
    consultar_relaciones()