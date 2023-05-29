from package.Functions import *
import numpy as np

"""
Crea una matriz de 3x3 y llénala con números 
aleatorios del 10 al 20. Luego, encuentra la 
suma de todos los elementos de la matriz y 
muestra el resultado.
"""

cls()
print("Crea una matriz de 3x3 y llénala con números aleatorios del 10 al 20. Luego, encuentra la suma de todos los elementos de la matriz y muestra el resultado.\n")
mat1 = np.random.randint(10,21,(3,3))

print("Matriz: \n",mat1)
print("Suma: \n",np.sum(mat1))
