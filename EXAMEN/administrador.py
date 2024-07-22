from persona import Persona
from producto import Producto
from cliente import Cliente
from proveedor import Proveedor
from almacen import Almacen

class Administrador(Persona):
    def __init__(self, id, nombre, email):
        super().__init__(id, nombre, email)

    def gestionar(self, entidad):
        if isinstance(entidad, Producto):
            print(f"Producto {entidad.nombre} gestionado por {self.nombre}")
        elif isinstance(entidad, Cliente):
            print(f"Cliente {entidad.nombre} gestionado por {self.nombre}")
        elif isinstance(entidad, Proveedor):
            print(f"Proveedor {entidad.nombre} gestionado por {self.nombre}")
        elif isinstance(entidad, Almacen):
            print(f"Almacen {entidad.ubicacion} gestionado por {self.nombre}")
