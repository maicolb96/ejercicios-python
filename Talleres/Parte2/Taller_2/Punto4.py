from package.Functions import *
import numpy as np

"""
Crea una matriz de 3x3 y llénala 
con números aleatorios del 10 al 30.
"""

cls()
print("Este programa crea una matriz de 3x3 y la llena con números aleatorios del 10 al 30.\n")
mat = np.random.randint(10,31,(3,3))
print(mat)