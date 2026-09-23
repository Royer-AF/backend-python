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

laptop = Producto("Laptop Lenovo", 2500, 5)
laptop.vender(4)
laptop.vender(2)