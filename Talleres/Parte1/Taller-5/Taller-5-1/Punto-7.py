"""
Este programa llena un vector con múltiplos de 20 y luego 
permite al usuario realizar diferentes operaciones con 
los elementos del vector.
"""

import os
os.system("cls")

print("Este programa llena un vector con múltiplos de 20 y luego\n" 
      "permite al usuario realizar diferentes operaciones con\n"  
      "los elementos del vector.\n" )

# función para verificar si un número es múltiplo de 20
def es_multiplo_de_20(numero):
    return numero % 20 == 0

# inicializar el vector y llenarlo con múltiplos de 20
vector = []
for i in range(1, 101):
    if es_multiplo_de_20(i):
        vector.append(i)

# preguntar al usuario si desea promediar el vector
promediar = input("¿Desea promediar el vector? (S/N): ")
if promediar == "S" or promediar == "s":
    promedio = sum(vector) / len(vector)
    print("El promedio del vector es:", promedio)

# preguntar al usuario si desea mostrar la suma del vector
mostrar_suma = input("¿Desea mostrar la suma del vector? (S/N): ")
if mostrar_suma == "S" or mostrar_suma == "s":
    suma = sum(vector)
    print("La suma del vector es:", suma)

# preguntar al usuario si desea mostrar cada resultado de cada posición dividido por 2
dividir_por_2 = input("¿Desea mostrar cada resultado de cada posición dividido por 2? (S/N): ")
if dividir_por_2 == "S" or dividir_por_2 == "s":
    for i in range(len(vector)):
        resultado = vector[i] / 2
        print("El resultado de la posición", i, "dividido por 2 es:", resultado)
