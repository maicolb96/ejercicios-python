"""
Un programa que pida al usuario los datos 
de una matriz de 3x3, y calcule y muestre 
su matriz adjunta.
"""
import os
os.system("cls")

print("Este algoritmo calcula la matriz adjunta de una matriz 3x3.\n")

matriz = [[int(input(f"Ingrese el valor para la posición [{i},{j}]: ")) for j in range(3)] for i in range(3)]
adjunta = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        submatriz = [[0 for k in range(2)] for l in range(2)]
        for k in range(2):
            for l in range(2):
                fila = (i + k + 1) % 3
                columna = (j + l + 1) % 3
                submatriz[k][l] = matriz[fila][columna]
        determinante = submatriz[0][0]*submatriz[1][1] - submatriz[0][1]*submatriz[1][0]
        adjunta[j][i] = (-1)**(i+j) * determinante

os.system("cls")
print("La matriz original es: ")
for row in matriz:print(row)
print("\nLa matriz adjuna es: ")
for row in adjunta:print(row)        