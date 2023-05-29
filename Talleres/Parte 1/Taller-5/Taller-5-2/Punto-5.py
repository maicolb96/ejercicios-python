"""
Un programa que use una matriz de 3x4 para resolver un sistema 
de 3 ecuaciones con 3 incógnitas usando el método de Gauss 
(hacer ceros por debajo de la diagonal principal para luego 
aplicar sustitución regresiva).
"""
import os
os.system("cls")

print("Este algoritmo usa una matriz de 3x4 para resolver un sistema\n" 
      "de 3 ecuaciones con 3 incógnitas usando el método de Gauss.\n")

matriz = [[int(input(f"Ingrese el valor para la posición [{i},{j}]: ")) for j in range(4)] for i in range(3)]
os.system("cls")

try:
    for i in range(3):
        for j in range(i+1, 3):
            factor = matriz[j][i] / matriz[i][i]
            for k in range(i, 4):
                matriz[j][k] -= factor * matriz[i][k]
    
    x = [0, 0, 0]
    for i in range(2, -1, -1):
        suma = 0
        for j in range(i+1, 3):
            suma += matriz[i][j] * x[j]
        x[i] = (matriz[i][3] - suma) / matriz[i][i]
    
    print(f"Las soluciones son: x={x[0]:.2f}, y={x[1]:.2f}, z={x[2]:.2f}")
except ValueError as e:
    if "float division by zero" in str(e):
        print("Error, hay una divición por cero imposible de resolver.")