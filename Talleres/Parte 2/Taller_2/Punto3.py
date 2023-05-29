from package.Functions import *
import numpy as np

"""
Crea una matriz de 2x2 
y llénala con números 
aleatorios del 1 al 20.
"""

cls()
print("Este programa crea una matriz de 2x2 y la llena con números aleatorios del 1 al 20.\n")
mat = np.random.randint(1,20,(2,2))
print(mat)