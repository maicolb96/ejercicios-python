"""
En un supermercado se requiere un sistema que almacene los 
siguientes datos de sus productos: nombre del producto, 
marca, tamaño, precio, y unidades existentes. 

Para ello Defina. 

 Tipos de datos 
 Vector 
 Defina un registro que defina el vector y un campo adicional 
 Escribe las subrutinas necesarias para realizar las siguientes operaciones 

1. Agregar: Consiste en introducir nuevos productos 
            con todos sus datos, se pueden ingresar varios 
            productos consecutivamente, deteniendo el proceso 
            cuando se introduzca un producto cuyo nombre comience 
            por un caracter especial. 

2. Consulta por producto: solicitando el nombre y mostrando todos 
                          sus datos y el total 

3. Reporte de productos: muestra el listado de todos los productos 
                         con sus datos, añada el costo total por 
                         producto y el costo total del inventario. 

El programa debe estar comandado por un menú con las operaciones 
descritas anteriormente 

"""

import os
os.system("cls")


from collections import namedtuple
Producto = namedtuple('Producto', ['nombre', 'marca', 'tamaño', 'precio', 'existencias'])

MAX_PRODUCTOS = 100
productos = [None] * MAX_PRODUCTOS
n_productos = 0

def agregar_producto():
    global n_productos
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre.startswith("!"):
            break
        marca = input("Ingrese la marca del producto: ")
        tamaño = input("Ingrese el tamaño del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        existencias = int(input("Ingrese las unidades existentes del producto: "))
        productos[n_productos] = Producto(nombre, marca, tamaño, precio, existencias)
        n_productos += 1
        os.system("cls")

def buscar_producto(nombre):
    total = 0
    for i in range(n_productos):
        if productos[i].nombre == nombre:
            print(f"Nombre: {productos[i].nombre}")
            print(f"Marca: {productos[i].marca}")
            print(f"Tamaño: {productos[i].tamaño}")
            print(f"Precio: {productos[i].precio}")
            print(f"Existencias: {productos[i].existencias}")
            total += productos[i].precio * productos[i].existencias
    print(f"Total de {nombre}: {total}")
    

def reporte_productos():
    total_inventario = 0
    for i in range(n_productos):
        print(f"Nombre: {productos[i].nombre}")
        print(f"Marca: {productos[i].marca}")
        print(f"Tamaño: {productos[i].tamaño}")
        print(f"Precio: {productos[i].precio}")
        print(f"Existencias: {productos[i].existencias}")
        costo_producto = productos[i].precio * productos[i].existencias
        print(f"Costo total del producto: {costo_producto}")
        total_inventario += costo_producto
    print(f"Costo total del inventario: {total_inventario}")


# Menú principal
while True:
    print("Menú de opciones:")
    print("1. Agregar producto")
    print("2. Consulta por producto")
    print("3. Reporte de productos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    os.system("cls")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto(nombre)
    elif opcion == "3":
        reporte_productos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
