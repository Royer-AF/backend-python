# Clase Padre (General)
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_perfil(self):
        print(f"Usuario: {self.nombre} | Correo: {self.correo}")

# Clase Hija (Especializada) que hereda de Usuario
class Administrador(Usuario):
    def __init__(self, nombre, correo, nivel_acceso):
        # super() llama al __init__ de la clase Padre
        super().__init__(nombre, correo) 
        self.nivel_acceso = nivel_acceso

    def borrar_cuenta(self, usuario):
        print(f"El admin {self.nombre} ha eliminado la cuenta de {usuario}.")

# Uso
admin1 = Administrador("Carlos", "carlos@upc.edu.pe", nivel_acceso=5)
admin1.mostrar_perfil()  # Método heredado de Usuario
admin1.borrar_cuenta("Juan123")  # Método propio de Administrador