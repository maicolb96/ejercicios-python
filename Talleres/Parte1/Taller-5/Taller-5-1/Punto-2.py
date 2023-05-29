"""
Realizar Un vector capaz de almacenar por sí solo los 
siguientes números:

2,4,6,8,10,12,14,16,18,20,22,24,26,28,30.
"""
import os
os.system("cls")

print("El algoritmo crea un vector dimensión 20, que sea capaz por si solo\n" 
       "de guardar la siguiente sucesiones de números\n"
       "2,4,6,8,10,12,14,16,18,20,22,24,26,28,30.\n")

vector=[i for i in range(2,31,2)]

print(f"El vector es: {vector}")
