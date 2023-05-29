from package.Functions import *

"""
14.rellenar una matriz identidad de 4x4
"""

def matriz_identidad():
    mat= [[1 if i==j else 0 for j in range(4)]for i in range(4)]
    print_mat(mat)

def print_mat(mat): 
    for m in mat:
        for i in m:
            print(i, end=" ")
        print() 

cls()
print("Este algoritmo imprime una matriz identidad 4x4.\n")
matriz_identidad()