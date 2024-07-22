from flask import Flask, render_template, request
from modelo import Modelo
from vista import Vista
from controlador import Controlador
from precio import Precio
from almacen import Almacen
from proveedor import Proveedor
from producto import Producto
from cliente import Cliente
from administrador import Administrador

app = Flask(__name__)

# Crear el modelo y la vista
modelo = Modelo()
vista = Vista()

# Crear el controlador
controlador = Controlador(modelo, vista)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    monto = float(request.form['monto'])
    moneda = request.form['moneda']
    descuento = float(request.form['descuento'])
    ubicacion = request.form['ubicacion']
    capacidad = int(request.form['capacidad'])
    proveedor_nombre = request.form['proveedor_nombre']
    proveedor_contacto = request.form['proveedor_contacto']

    precio = Precio(monto, moneda, descuento)
    almacen = Almacen(1, ubicacion, capacidad)
    proveedor = Proveedor(1, proveedor_nombre, proveedor_contacto)
    producto = Producto(1, nombre, descripcion, precio, almacen, proveedor)

    controlador.agregar_producto(producto)

    return "Producto agregado"

@app.route('/mostrar_productos')
def mostrar_productos():
    productos = modelo.productos
    return render_template('productos.html', productos=productos)

if __name__ == "__main__":
    app.run(debug=True)
