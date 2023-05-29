"""
Desarrolle un algoritmo con menú, funciones, variables 
globales, registros y archivo en disco para el control 
de inventario de los artículos en un almacén. 

Datos de cada artículo 

Código 
Nombre 
Cantidad actual del artículo

Menú 

1. Ingresar: Ingreso del nuevo artículo con la cantidad inicial 
2. Agregar: Agregar cantidad a un artículo existente 
3. Vender: Vender una cantidad de un artículo existente 
4. Consultar: Conocer la cantidad disponible de una artículo 
5. Salir 
"""
import os
os.system("cls")

import pickle

# Definición de la estructura de registro de artículo
class Articulo:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

# Definición de la lista global de artículos
articulos = []

# Definición de la función para guardar los artículos en archivo
def guardar_articulos():
    with open(r'Talleres\Taller-5\Taller-5-2\articulos.pickle', 'wb') as f:
        pickle.dump(articulos, f)

# Definición de la función para cargar los artículos desde archivo
def cargar_articulos():
    try:
        with open(r'Talleres\Taller-5\Taller-5-2\articulos.pickle', 'rb') as f:
            global articulos
            articulos = pickle.load(f)
    except FileNotFoundError:
        pass

# Función para agregar un nuevo artículo
def agregar_articulo():
    codigo = input('Ingrese el código del artículo: ')
    nombre = input('Ingrese el nombre del artículo: ')
    cantidad = int(input('Ingrese la cantidad inicial del artículo: '))
    articulos.append(Articulo(codigo, nombre, cantidad))
    guardar_articulos()
    print('El artículo se ha agregado correctamente.')

# Función para agregar cantidad a un artículo existente
def agregar_cantidad():
    codigo = input('Ingrese el código del artículo: ')
    articulo_encontrado = False
    for articulo in articulos:
        if articulo.codigo == codigo:
            cantidad = int(input('Ingrese la cantidad a agregar: '))
            articulo.cantidad += cantidad
            guardar_articulos()
            print(f'Se han agregado {cantidad} unidades al artículo {articulo.nombre}.')
            articulo_encontrado = True
            break
    if not articulo_encontrado:
        print('No se ha encontrado el artículo con el código ingresado.')

# Función para vender una cantidad de un artículo existente
def vender_articulo():
    codigo = input('Ingrese el código del artículo: ')
    articulo_encontrado = False
    for articulo in articulos:
        if articulo.codigo == codigo:
            cantidad = int(input('Ingrese la cantidad a vender: '))
            if cantidad <= articulo.cantidad:
                articulo.cantidad -= cantidad
                guardar_articulos()
                print(f'Se han vendido {cantidad} unidades del artículo {articulo.nombre}.')
            else:
                print(f'No hay suficientes unidades del artículo {articulo.nombre}.')
            articulo_encontrado = True
            break
    if not articulo_encontrado:
        print('No se ha encontrado el artículo con el código ingresado.')

# Función para consultar la cantidad disponible de un artículo
def consultar_cantidad():
    codigo = input('Ingrese el código del artículo: ')
    articulo_encontrado = False
    for articulo in articulos:
        if articulo.codigo == codigo:
            print(f'El artículo {articulo.nombre} tiene {articulo.cantidad} unidades disponibles.')
            articulo_encontrado = True
            break
    if not articulo_encontrado:
        print('No se ha encontrado el artículo con el código ingresado.')

# Función principal para mostrar el menú y procesar la opción seleccionada
def menu():
    cargar_articulos()
    while True:
        print('\n-------- MENÚ --------')
        print('1. Ingresar artículo')
        print('2. Agregar cantidad a un artículo')
        print('3. Vender artículo')
        print("4. Consultar la cantidad disponible de un artículo")
        print("5. Salir del programa")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            agregar_articulo()
        elif opcion == 2:
            agregar_cantidad()
        elif opcion == 3:
            vender_articulo()
        elif opcion == 4:
            consultar_cantidad()
        elif opcion == 5:
            print("Gracias por utilizar el sistema de control de inventario.")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

menu()


