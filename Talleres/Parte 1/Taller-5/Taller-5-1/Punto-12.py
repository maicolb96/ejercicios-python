"""
Este programa permite leer una secuencia de 
números y sumar solo los pares, mostrando 
el resultado del proceso.
"""

import os
os.system("cls")

print("Este programa permite leer una secuencia de\n" 
      "números y sumar solo los pares, mostrando\n"
      "el resultado del proceso.\n")

# inicializar una variable de suma
suma_pares = 0

# leer los números hasta que el usuario ingrese un número negativo
while True:
    # pedir al usuario que ingrese un número
    numero = int(input("Ingrese un número (o un número negativo para terminar): "))
    # si el número es negativo, salir del bucle
    if numero < 0:
        break
    # si el número es par, agregarlo a la suma de pares
    if numero % 2 == 0:
        suma_pares += numero
    # mostrar la suma de pares actual
    print("La suma de los pares es:", suma_pares)

# mostrar la suma final de los pares
print("La suma final de los pares es:", suma_pares)
