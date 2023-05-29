"""
Este programa permite llenar un vector de 30 números por el usuario, 
calcular el promedio de los números, indicar el menor, el mayor y 
los números que son múltiplos de 2.
"""

import os
os.system("cls")

print("Este programa permite llenar un vector de 30 números\n"
      "por el usuario, calcular el promedio de los números,\n"
      "indicar el menor, el mayor y los números que son múltiplos de 2.\n"
      )

# inicializar un vector vacío de 30 elementos
numeros = []

# pedir al usuario que ingrese 30 números y almacenarlos en el vector
for i in range(30):
    numero = int(input(f"{i+1}) Ingrese un número: "))
    numeros.append(numero)

os.system("cls")   

# calcular el promedio
promedio = sum(numeros) / len(numeros)

# encontrar el menor número
menor = min(numeros)

# encontrar el mayor número
mayor = max(numeros)

# encontrar los números que son múltiplos de 2
multiplos_de_2 = [numero for numero in numeros if numero % 2 == 0]

# imprimir los resultados
print("El promedio de los números es:", promedio)
print("El número menor es:", menor)
print("El número mayor es:", mayor)
print("Los números que son múltiplos de 2 son:", multiplos_de_2)
