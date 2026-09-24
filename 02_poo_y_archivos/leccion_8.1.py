import json


cursos = [
    {"id": "001", "nombre": "Python Pro", "precio": 150},
    {"id": "002", "nombre": "JavaScript", "precio": 120},
    {"id": "003", "nombre": "Cobol", "precio": 100}
]


with open("inventario.json", "w", encoding="utf-8") as archivo:
    json.dump(cursos, archivo, ensure_ascii=False, indent=4)


with open("inventario.json", "r", encoding="utf-8") as archivo:
    productos_cargados = json.load(archivo)


for i in productos_cargados:
    print(f"Producto {i['id']}: {i['nombre']} - S/ {i['precio']:,.2f}")