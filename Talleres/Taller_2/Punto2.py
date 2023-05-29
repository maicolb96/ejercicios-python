from package.Functions import *
import numpy as np

"""
Crea un vector de tamaño 10 
y llénalo con números aleatorios 
del 50 al 100.
"""

cls()
print("Este programa crea un vector de tamaño 10 y lo llena con números aleatorios del 50 al 100.\n")
array = np.random.randint(50,101,10)
print(f"Array: {array}")