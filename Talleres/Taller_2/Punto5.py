from package.Functions import *
import numpy as np

"""
Crea dos vectores de tamaño 5 y llénalos
con números aleatorios del 1 al 5. 
Luego, suma los dos vectores y 
muestra el resultado.
"""

cls()
print("Este programa crea dos vectores de tamaño 5 y los llena con números aleatorios del 1 al 5. Luego, suma los dos vectores y muestra el resultado.\n")
vect1 = np.random.randint(1,6,5)
vect2 = np.random.randint(1,6,5)

print(f"V1: {vect1}")
print(f"V2: {vect2}")
print(f"SM: {vect1+vect2}")