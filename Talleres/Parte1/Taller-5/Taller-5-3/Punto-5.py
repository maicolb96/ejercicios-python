"""
Imprimir de la siguiente matriz la diagonal principal:

25 12 26 7 15
12 12 2 9 25
25 6 4 25 6
1 4 6 10 9
2 25 8 5 8
"""
import os
os.system("cls")

matriz=[[25,12,26,7,15],
        [12,12,2,9,25],
        [25,6,4,25,6],
        [1,4,6,10,9],
        [2,25,8,5,8]]

print("La matriz es: \n")
for row in matriz:print(row)
print("\nLa diagonal de la matriz es: ")
for i in range(len(matriz)):print(matriz[i][i], end=" ")