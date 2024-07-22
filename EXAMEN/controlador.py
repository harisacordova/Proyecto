from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_producto(self, producto):
        self.modelo.agregar_producto(producto)

    def agregar_cliente(self, cliente):
        self.modelo.agregar_cliente(cliente)

    def mostrar_productos(self):
        productos = self.modelo.productos
        self.vista.mostrar_productos(productos)

    def mostrar_clientes(self):
        clientes = self.modelo.clientes
        self.vista.mostrar_clientes(clientes)
