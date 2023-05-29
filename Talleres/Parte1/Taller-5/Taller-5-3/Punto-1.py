"""
1). Realizar una matriz de 5*5 y llenarlo 
con los siguientes datos:

25 12 26 7 15
12 12 2  9 25
25 6  4  25 6
1  4  6  10 9
2  25 8  5  8

*Debe sumar todos los números ingresados.
*Cuando la matriz este llena, deben contar de cada número cuantos hay repetidos y llenar
un vector con esa información imprimiéndolo en pantalla, ejemplo: el número 25 se
repite 5 veces.

"""
import os
import numpy as np
os.system("cls")

matriz = [[25,12,26,7,15],
          [12,12,2,9,25],
          [25,6,4,25,6],
          [1,4,6,10,9],
          [2,25,8,5,8]]

print("La matriz es la siguiente:\n")
for row in matriz: print(row)    
print(f"\nLa suma de todos los números de la matriz es: {np.sum(matriz)}")

contador = {}
for i in range(5):
    for j in range(5):
        num = matriz[i][j]
        if num not in contador:
            contador[num] = 1
        else:
            contador[num] += 1

repetidos = [num for num in contador if contador[num] > 1]

print("Matriz:")
for fila in matriz:
    print(fila)

print("Cantidad de veces que aparece cada número:")
for num in contador:
    print(num, "-", contador[num])

print("Números repetidos en la matriz:", repetidos)

