from package.Functions import *
import numpy as np

"""
Crea una matriz de 3x3 y otra matriz de 3x3. 
Llénalas con números aleatorios del 10 al 20. 
Luego, resta las dos matrices y muestra el resultado.
"""

cls()
print("Este programa crea una matriz de 3x3 y otra matriz de 3x3.\n Llénalas con números aleatorios del 10 al 20.\n Luego, resta las dos matrices y muestra el resultado.\n")
mat1 = np.random.randint(10,21,(3,3))
mat2 = np.random.randint(10,21,(3,3))

print("Matriz1: \n",mat1)
print("Matriz2: \n",mat2)
print("Resta: \n",mat1-mat2)