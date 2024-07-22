class Proveedor:
    def __init__(self, id, nombre, contacto):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto

    def entregar_producto(self, producto):
        print(f"Producto {producto.nombre} entregado por {self.nombre}")
