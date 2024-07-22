from modelo import Modelo
from vista import Vista
from controlador import Controlador
from precio import Precio
from almacen import Almacen
from proveedor import Proveedor
from producto import Producto
from cliente import Cliente
from administrador import Administrador

if __name__ == "__main__":
    # Crear el modelo y la vista
    modelo = Modelo()
    vista = Vista()
    
    # Crear el controlador
    controlador = Controlador(modelo, vista)

    # Crear algunos objetos
    precio1 = Precio(100.0, "USD", 0.1)
    almacen1 = Almacen(1, "Bogotá", 100)
    proveedor1 = Proveedor(1, "Proveedor1", "contacto@proveedor1.com")
    producto1 = Producto(1, "Producto1", "Descripción1", precio1, almacen1, proveedor1)
    cliente1 = Cliente(1, "Cliente1", "Calle 123", "cliente1@correo.com")
    administrador1 = Administrador(1, "Administrador1", "admin@correo.com")

    # Usar el controlador para agregar y mostrar objetos
    controlador.agregar_producto(producto1)
    controlador.agregar_cliente(cliente1)
    
    controlador.mostrar_productos()
    controlador.mostrar_clientes()

    # Ejemplo de polimorfismo
    administrador1.gestionar(producto1)
    administrador1.gestionar(cliente1)
    administrador1.gestionar(proveedor1)
    administrador1.gestionar(almacen1)
