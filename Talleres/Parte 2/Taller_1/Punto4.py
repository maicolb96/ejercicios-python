from package.Functions import *
import numpy as np

"""
Diseñar una función que encuentro el 
mayor de dos números enteros.
"""

#Función que recibe un vector de dimension 2 y por medio de la función max de
#numpy calcula el mayor y lo retorna
def mayor(n):
    return np.max(n)

#Se limpia la consola
cls()

#Se ecplica que hace el programa
print("Este programa imprime el mayor de dos números.\n")

#Se leen los 2 números y se almacenan en un vector por medio de la Compresión de listas
v=[int(input(f"Ingrese el número #{i}: \n")) for i in range(1,3,1)]

#Se llama la función mayor y se imprime su retorno.
print(f"\nEl mayor entre {v[0]} y {v[1]} es {mayor(v)}")
