"""
Un programa que pida al usuario los datos de dos
matrices de 2x2, y calcule y muestre su producto.
"""
import os
os.system("cls")

print("Este algoritmo pide al usuario los datos de dos matrices de 2x2, y calcule y muestre su producto.\n")

# Pedimos al usuario los datos de las matrices
matriz1 = [[int(input(f"Ingrese el valor para la posición [{i},{j}] de la matriz 1: ")) for j in range(2)] for i in range(2)]
matriz2 = [[int(input(f"Ingrese el valor para la posición [{i},{j}] de la matriz 2: ")) for j in range(2)] for i in range(2)]
producto = []
producto = [[matriz1[i][0]*matriz2[0][j] + matriz1[i][1]*matriz2[1][j] for j in range(2)] for i in range(2)]

os.system("cls")
print("La matriz 1 es: ")
for row in matriz1:print(row)
print("\nLa matriz 2 es:")
for row in matriz2: print(row)
print("\nLa multiplicación de matrices es:")
for row in producto: print(row)
