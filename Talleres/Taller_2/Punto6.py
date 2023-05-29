from package.Functions import *
import numpy as np

"""
Crea dos vectores de tamaño 6 y 
llénalos con números aleatorios 
del 1 al 10. Luego, resta los dos 
vectores y muestra el resultado.
"""
cls()
print("Este programa crea dos vectores de tamaño 6 y los llena con números aleatorios del 1 al 10. Luego, resta los dos vectores y muestra el resultado.\n")
vect1 = np.random.randint(1,11,6)
vect2 = np.random.randint(1,11,6)

print(f"V1: {vect1}")
print(f"V2: {vect2}")
print(f"RE: {vect1-vect2}")