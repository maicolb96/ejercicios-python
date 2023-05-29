from package.Functions import *
import numpy as np

"""
Crea un vector de tamaño 5 y llénalo con números
aleatorios del 1 al 10. Luego, multiplica los 
elementos del vector por 2 y muestra el resultado.
"""

cls()
print("Crea un vector de tamaño 5 y llénalo con números aleatorios del 1 al 10. Luego, multiplica los elementos del vector por 2 y muestra el resultado.\n")
array = np.random.randint(1,11,5)

print(f"Vector: {array}")
print(f"Vector * 2: {array*2}")