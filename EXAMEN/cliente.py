from persona import Persona

class Cliente(Persona):
    def __init__(self, id, nombre, direccion, email):
        super().__init__(id, nombre, email)
        self.direccion = direccion

    def comprar_producto(self, producto):
        print(f"Cliente {self.nombre} compró el producto {producto.nombre}")
