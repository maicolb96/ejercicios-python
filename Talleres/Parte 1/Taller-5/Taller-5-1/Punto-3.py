"""
Realizar Un vector capaz de almacenar por sí solo los 
siguientes números:

1,2,6,9,12,15,18,21,24,27,30.
"""
import os
os.system("cls")

print("El algoritmo crea un vector dimensión 20, que sea capaz por si solo\n" 
       "de guardar la siguiente sucesiones de números\n"
       "1,2,6,9,12,15,18,21,24,27,30.\n")

vector=[1,2,6]
vector+=([i for i in range(9,33,3)])

print(f"El vector es: {vector}")
