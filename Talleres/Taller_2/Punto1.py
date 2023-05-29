from package.Functions import *
import numpy as np

"""
Crea un vector de tamaño 5 y llénalo con 
números aleatorios del 1 al 10.
"""

cls()
print("Este programa crea un vector de tamaño 5 y lo llena con números aleatorios del 1 al 10.\n")
array = np.random.randint(1,11,5)
print(f"Vector: {array}")