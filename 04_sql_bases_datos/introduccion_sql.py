
import sqlite3

conexion = sqlite3.connect("mi_tienda.db")
cursor = conexion.cursor()

# 1. Crear la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
""")

# 2. Limpiar la tabla antes de insertar para evitar duplicados en cada prueba
cursor.execute("DELETE FROM productos")

# 3. Insertar varios productos de un solo golpe con executemany
nuevos_productos = [
    ('Monitor 24 pulgadas', 650.00),
    ('Audífonos Bluetooth', 120.00),
    ('Cargador Carga Rápida', 45.00)
]

cursor.executemany("""
INSERT INTO productos (nombre, precio) 
VALUES (?, ?)
""", nuevos_productos)

# 4. Guardar cambios
conexion.commit()

# 5. Consultar filtrando solo productos con precio mayor a S/ 50.00
cursor.execute("SELECT * FROM productos WHERE precio > 50.00")
productos_filtrados = cursor.fetchall()

print("--- PRODUCTOS DE MÁS DE S/ 50.00 ---")
for prod in productos_filtrados:
    print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: S/ {prod[2]:,.2f}")

conexion.close()
