from producto import Producto
from cliente import Cliente
from proveedor import Proveedor
from almacen import Almacen

class Modelo:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.proveedores = []
        self.almacenes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def agregar_almacen(self, almacen):
        self.almacenes.append(almacen)
