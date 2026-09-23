class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.activo = True

    def desactivar_cuenta(self):
        self.activo = False
        print(f"La cuenta de {self.nombre} ha sido desactivada.")


usuario1 = Usuario("Carlos", "carlos@upc.edu.pe")
print(f"Usuario: {usuario1.nombre} | Estado: {usuario1.activo}")

usuario1.desactivar_cuenta()