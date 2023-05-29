"""
De una matriz 5*5 llenar la diagonal segundaria
con la letra E

"""
import os,random
os.system("cls")

matriz=[[random.randint(0, 50) for _ in range(5)]for _ in range(5)]

print("La matriz original es: \n")
for row in matriz:print(row)
print("\nLa matriz con la diagonal reemplazada por A es: \n")
for i in range(len(matriz)):matriz[i][i]="E"
for row in matriz:print(row)