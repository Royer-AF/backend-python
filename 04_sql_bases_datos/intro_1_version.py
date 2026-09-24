import sqlite3

# 1. Conectar a la base de datos (si el archivo no existe, SQLite lo crea automáticamente)
conexion = sqlite3.connect("mi_tienda.db")

# 2. Crear un cursor (es el "puntero" que ejecuta los comandos SQL)
cursor = conexion.cursor()

# 3. Crear una tabla llamada 'productos' usando SQL puro
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
""")

# 4. Insertar datos usando el comando SQL 'INSERT'
cursor.execute("""
INSERT INTO productos (nombre, precio) 
VALUES ('Monitor 24 pulgadas', 650.00)
""")
cursor.execute("""
INSERT INTO productos (nombre, precio)
VALUES ('Audífonos', 80)
""")
cursor.execute("""
INSERT INTO productos (nombre, precio)
VALUES ('Cargador', 50)
""")

# 5. Guardar los cambios en el archivo de la base de datos
conexion.commit()

# 6. Consultar los datos guardados usando el comando SQL 'SELECT'
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()  # Obtiene todas las filas devueltas

print("--- PRODUCTOS EN LA BASE DE DATOS ---")
for prod in productos:
    print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: S/ {prod[2]}")

# 7. Cerrar la conexión
conexion.close()
