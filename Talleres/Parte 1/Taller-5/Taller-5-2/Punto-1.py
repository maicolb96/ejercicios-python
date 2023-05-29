"""
Un programa pida datos al usuario los datos de una 
matriz de 2x2 y muestra su traspuesta (el resultado 
de intercambiar filas por columnas).
"""
import os
os.system("cls")

print("Este algoritmo muestra la matriz traspuesta de una matriz 2x2")

# Creamos la matriz
matrix = [[int(input(f"Ingrese el valor para la posición [{i},{j}]: ")) for j in range(2)] for i in range(2)]
inversa=[[matrix[j][i] for j in range(2)]for i in range(2)]

os.system("cls")
# Mostramos la matriz resultante
print("Matriz original")
for row in matrix: print(row)
print("\nMatriz inversa")
for row in inversa: print(row)

    
