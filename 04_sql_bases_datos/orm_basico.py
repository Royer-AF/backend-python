from sqlmodel import Field, Session, SQLModel, create_engine, select

# 1. Definimos el modelo de la tabla como una clase de Python


class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float


# 2. Creamos el motor de conexión a la base de datos SQLite
sqlite_file_name = "04_sql_bases_datos/tienda_orm.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# echo=True nos muestra en consola los comandos SQL reales que genera SQLModel por detrás
engine = create_engine(sqlite_url, echo=True)

# 3. Función para crear las tablas en la base de datos


def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)

# 4. Función para insertar un registro


def crear_producto():
    prod1 = Producto(nombre="Teclado Mecánico", precio=280.00)
    prod2 = Producto(nombre="Silla Gamer", precio=540)

    # La Sesión maneja la transacción con la base de datos
    with Session(engine) as session:
        session.add(prod1)     # Equivale al INSERT INTO
        session.add(prod2)
        session.commit()      # Guarda los cambios
        session.refresh(prod1)  # Carga el ID generado automáticamente
        session.refresh(prod2)
        print(f"--> Producto creado con ID: {prod1.id}")
        print(f"--> Producto creado con ID: {prod2.id}")

# 5. Función para consultar datos


def obtener_productos():
    with Session(engine) as session:
        statement = select(Producto)  # Equivale a SELECT * FROM producto
        resultados = session.exec(statement).all()

        print("\n--- PRODUCTOS DESDE EL ORM ---")
        for producto in resultados:
            print(
                f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: S/ {producto.precio}")


if __name__ == "__main__":
    crear_db_y_tablas()
    crear_producto()
    obtener_productos()
