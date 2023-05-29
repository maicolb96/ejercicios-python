"""
Un programa que pida al usuario los datos de 
una matriz de 3x3, y calcule y muestre su
matriz inversa.
"""
import os
os.system("cls")

print("Este algoritmo calcula la matriz inversa de una matriz 3x3.\n")

matriz = [[int(input(f"Ingrese el valor para la posición [{i},{j}]: ")) for j in range(3)] for i in range(3)]
os.system("cls")

det = matriz[0][0] * (matriz[1][1]*matriz[2][2] - matriz[1][2]*matriz[2][1]) - \
      matriz[0][1] * (matriz[1][0]*matriz[2][2] - matriz[1][2]*matriz[2][0]) + \
      matriz[0][2] * (matriz[1][0]*matriz[2][1] - matriz[1][1]*matriz[2][0])

if det == 0:
    print("\nLa matriz es singular, no tiene matriz inversa.")
    exit()

cofactores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        submatriz = [[matriz[m][n] for n in range(3) if n != j] for m in range(3) if m != i]
        cofactor = (-1)**(i+j) * (submatriz[0][0] * submatriz[1][1] - submatriz[0][1] * submatriz[1][0])
        cofactores[i][j] = cofactor
adjunta = [[cofactores[j][i] for j in range(3)] for i in range(3)]
inversa = ([['{:.2f}'.format(adjunta[i][j] / det) for j in range(3)] for i in range(3)])

os.system("cls")
print("La matriz original es: ")
for row in matriz:print(row)
print("\nLa matriz inversa es:")
for fila in inversa: print(fila)