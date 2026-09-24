# Un diccionario guarda pares de clave-valor
usuario = {
    "nombre": "Carlos",
    "email": "carlos@upc.edu.pe",
    "es_estudiante": True
}

# Acceder a un valor por su clave
print(usuario["email"])


import json

datos = {
    "proyecto": "Tienda Online",
    "version": 1.0,
    "activo": True
}

# Guardar en un archivo físico (.json)
with open("config.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

# Leer desde el archivo físico
with open("config.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(datos_cargados["proyecto"])