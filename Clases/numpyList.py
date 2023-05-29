import numpy as np

#Llenar una matriz numpy por teclado
matriz = np.zeros((2,5))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i,j] = input(f"Ingrese el valor {i,j}: ")

matriz_ordenada = np.sort(np.sort(matriz, axis=1), axis=0)

print(matriz_ordenada)