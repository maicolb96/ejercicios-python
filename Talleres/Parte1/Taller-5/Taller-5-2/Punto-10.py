"""
En la biblioteca de la facultad de ingeniería, se quiere 
almacenar en un vector de 10 elementos 8 grandes áreas o 
disciplinas, en orden alfabético, para ello se requiere 
construir un programa que permita insertar las áreas y 
además los libros que pertenezcan a cada una de ellas 
para el año 2014. El algoritmo debe presentar la 
cantidad de libros en cada una de las áreas, además 
de un rango entre las cantidades mínimas y máximas 
adquiridas durante el año 2014 en cada disciplina. 
"""

import os
os.system("cls")

boletas_disponibles = 100
boletas_vendidas = 0
cedulas_vendidas = []

while boletas_disponibles > 0:
    cedula = input("Ingrese el número de cédula del comprador: ")
    if cedula in cedulas_vendidas:
        print("Lo sentimos, la venta de boletas para esta persona ya ha sido registrada.")
        continue
    cedulas_vendidas.append(cedula)
    
    cantidad_boletas = int(input("Ingrese la cantidad de boletas que desea comprar (máximo 4): "))
    if cantidad_boletas < 1 or cantidad_boletas > 4:
        print("La cantidad de boletas ingresada no es válida. Intente de nuevo.")
        continue
    elif cantidad_boletas > boletas_disponibles:
        print(f"Lo sentimos, sólo quedan {boletas_disponibles} boletas disponibles.")
        continue
    
    boletas_vendidas += cantidad_boletas
    boletas_disponibles -= cantidad_boletas
    print(f"Compra exitosa. Se han vendido {cantidad_boletas} boletas. Quedan {boletas_disponibles} boletas disponibles.")
    
print("Se han vendido todas las boletas disponibles. La venta ha finalizado.")
