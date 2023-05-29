"""
Tenemos estas dos matrices A Y B:

a = |6  1|  b = |7 -2|
    |8 -2|      |-1 4|
"""
import numpy as np
import os
os.system("cls")

A=[[6,1],[8,-2]]
B=[[7,-2],[-1,4]]

print("La matriz A es: \n")
for row in A:print(row)
print("\nLa matriz B es: \n")
for row in B:print(row)
print("\nLa suma de la matriz A + B es: \n")
for row in np.add(A,B):print(row)