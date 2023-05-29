from package.Functions import *
import numpy as np

"""
Crea una matriz de 2x2 y llénala con números 
aleatorios del 1 al 10. Luego, encuentra el 
valor máximo y mínimo de la matriz y muestra 
los resultados.
"""

cls()
print("Crea una matriz de 2x2 y llénala con números aleatorios del 1 al 10. Luego, encuentra el valor máximo y mínimo de la matriz y muestra los resultados.\n")
mat1 = np.random.randint(1,11,(2,2))

print("Matriz: \n",mat1)
print("Maximo: \n",np.max(mat1))
print("Mínimo: \n",np.min(mat1))