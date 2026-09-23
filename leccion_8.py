import json


curso = {
    "nombre": "Python Pro",
    "precio": 49.00,
    "horas_duracion": 50
}


with open("3.1_curso.json", "w") as archivo:
    json.dump(curso, archivo, indent=4)
print("Curso guardado.")


with open("3.1_curso.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(f"- {datos_cargados['nombre']} | Precio: {datos_cargados['precio']}")