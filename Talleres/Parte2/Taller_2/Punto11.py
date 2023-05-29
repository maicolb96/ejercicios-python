from package.Functions import *
import numpy as np

"""
Crea una matriz de 2x2 y llénala con números 
aleatorios del 1 al 10. Luego, multiplica cada 
elemento de la matriz por 3 y muestra el resultado.
"""

cls()
print("Crea una matriz de 2x2 y llénala con números aleatorios del 1 al 10. Luego, multiplica cada elemento de la matriz por 3 y muestra el resultado.\n")
mat1 = np.random.randint(1,11,(2,2))

print("Matriz: \n",mat1)
print("Matriz * 3: \n",mat1*3)
