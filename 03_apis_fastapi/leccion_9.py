from fastapi import FastAPI

app = FastAPI()

# Ruta 1: Inicio
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API"}

# Ruta 2: Información del programador
@app.get("/perfil")
def obtener_perfil():
    return {
        "estudiante": "Ingeniero de Sistemas",
        "lenguaje": "Python",
        "sistema": "Linux Mint XFCE"
    }

# Ruta 3: Estado de la tienda
@app.get("/tienda/estado")
def estado_tienda():
    return {"abierto": True, "moneda": "PEN"}


@app.get("/contacto")
def obtener_contacto():
    return {"correo": "example@gmail.com.ro",
            "ciudad": "Ayacucho"
    }