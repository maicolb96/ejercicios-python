"""
Este programa permite leer una secuencia de números, 
hasta que se introduce un número negativo y
mostrar la suma de dichos números.
"""

import os
os.system("cls")

print("Este programa permite leer una secuencia de números,\n" 
      "hasta que se introduce un número negativo y\n"
      "mostrar la suma de dichos números.\n")

# inicializar una variable de suma
suma = 0

# pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# leer la secuencia de números hasta que se ingresa un número negativo
while numero >= 0:
    # agregar el número a la suma
    suma += numero
    # pedir al usuario que ingrese otro número
    numero = int(input("Ingrese otro número: "))

# imprimir la suma de los números
print("La suma de los números es:", suma)
