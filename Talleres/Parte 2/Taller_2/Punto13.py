from package.Functions import *
import numpy as np

"""
Crea un vector de tamaño 5 y llénalo con 
números aleatorios del 1 al 10. Luego, 
encuentra el valor máximo y mínimo del 
vector y muestra los resultados.
"""

cls()
print("Crea un vector de tamaño 5 y llénalo con números aleatorios del 1 al 10. Luego, encuentra el valor máximo y mínimo del vector y muestra los resultados.\n")
array = np.random.randint(1,11,5)
print(f"Vector: {array}")
print(f"Maximo: {np.max(array)}")
print(f"Minimo: {np.min(array)}")