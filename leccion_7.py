class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta exitosa.")
            total = self.precio * cantidad
            print(f"Total a pagar: S/ {total:,.2f}")
        else:
            print("Stock insuficiente.")


class ProductoDigital(Producto):
    def __init__(self, nombre, precio, link_descarga):
        super().__init__(nombre, precio, stock=9999)
        self.link_descarga = link_descarga

    def descargar(self):
        print(f"Descargando {self.nombre} desde {self.link_descarga}")


licencia_python = ProductoDigital("Curso Python Pro", 49.90, "'https://upc.edu.pe/curso'")
licencia_python.vender(1)
licencia_python.descargar()
print("¡Gracias por su compra!")