from package.Functions import *
import numpy as np

"""
Crea una matriz de 2x2 y otra matriz de 2x2. 
Llénalas con números aleatorios del 1 al 10. 
Luego, suma las dos matrices y muestra el resultado.
"""

cls()
print("Este programa crea una matriz de 2x2 y otra matriz de 2x2.\n Las llena con números aleatorios del 1 al 10. \nLuego, suma las dos matrices y muestra el resultado.\n")
mat1 = np.random.randint(1,11,(2,2))
mat2 = np.random.randint(1,11,(2,2))

print("Matriz1: \n",mat1)
print("Matriz2: \n",mat2)
print("Suma: \n",mat1+mat2)