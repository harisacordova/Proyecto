class Vista:
    def mostrar_productos(self, productos):
        for producto in productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio.calcular_precio_final()}")

    def mostrar_clientes(self, clientes):
        for cliente in clientes:
            print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Email: {cliente.email}")
