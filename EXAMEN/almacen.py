class Almacen:
    def __init__(self, id, ubicacion, capacidad):
        self.id = id
        self.ubicacion = ubicacion
        self.capacidad = capacidad

    def almacenar_producto(self, producto):
        print(f"Producto {producto.nombre} almacenado en {self.ubicacion}")
