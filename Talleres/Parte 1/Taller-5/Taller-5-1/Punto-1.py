"""
Hacer un vector dimensión 20, que sea capaz por si solo 
de guardar la siguiente sucesiones de números:

1,3,5,7,9,11,13,15,17,19,21,23,25
"""

import os
os.system("cls")

print("El algoritmo crea un vector dimensión 20, que sea capaz por si solo\n" 
       "de guardar la siguiente sucesiones de números\n")

vector=[i for i in range(1,40,2)]

print(f"El vector es: {vector}")