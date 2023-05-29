import numpy as np
from package.Functions import *

"""
15.calcular la suma de los elementos de la diagonal
principal de una matriz de 4x4
"""     
    
def create_mat():
    mat= [[int(input(f"Ingrese el valor {i,j}: \n"))for j in range(4)]for i in range(4)]
    return mat

def print_mat(mat): 
    for m in mat:
        for i in m:
            print(i, end=" ")
        print() 

def sum_diag(mat):
    sum=[mat[i][j] if i==j else 0 for i in range(4) for j in range(4)]
    return sum

cls()
try:
    print("Este algoritmo imprime la suma de la diagonal ppal de una matriz 4x4.\n")
    mat=create_mat()
    cls()
    print("La matriz es: \n")
    print_mat(mat)
    print(f"\nLa suma de la diagonal ppal es: {np.sum(sum_diag(mat))}")
except ValueError as e:
    print(e)    


