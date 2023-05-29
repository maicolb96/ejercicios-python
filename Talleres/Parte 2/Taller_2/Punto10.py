from package.Functions import *
import numpy as np

"""
Crea un vector de tamaño 6 y llénalo con números 
aleatorios del 1 al 5. Luego, eleva cada elemento 
del vector al cuadrado y muestra el resultado.
"""

cls()
print("Crea un vector de tamaño 6 y llénalo con números aleatorios del 1 al 5. Luego, eleva cada elemento del vector al cuadrado y muestra el resultado.\n")
array = np.random.randint(1,6,6)

print(f"Vector: {array}")
print(f"Vector ^ 2: {array**2}")