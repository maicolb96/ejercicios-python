"""
Este programa permite leer una secuencia de números 
y mostrar su producto, el proceso finalizará cuando
el usuario pulsa la tecla n.
"""

import os
os.system("cls")

print("Este programa permite leer una secuencia de números \n"
      "y mostrar su producto, el proceso finalizará cuando\n"
      "el usuario pulsa la tecla n.\n")

# inicializar una variable de producto
producto = 1

# leer los números hasta que el usuario pulsa la tecla n
while True:
    # pedir al usuario que ingrese un número
    numero = input("Ingrese un número (o n para terminar): ")
    # si el usuario ingresa "n", salir del bucle
    if numero == "n":
        break
    # convertir el número a un número entero y multiplicarlo por el producto actual
    producto *= int(numero)

# imprimir el producto de los números
print("El producto de los números es:", producto)
