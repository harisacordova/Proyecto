from precio import Precio
from almacen import Almacen
from proveedor import Proveedor

class Producto:
    def __init__(self, id, nombre, descripcion, precio, almacen, proveedor):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.almacen = almacen
        self.proveedor = proveedor
