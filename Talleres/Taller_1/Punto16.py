from numpy import max
from package.Functions import *

"""
16.diseñar un algoritmo que calcule el mayor valor 
de una lista L de N elementos
"""
cls()
print("Este programa imprime el mayor de una lista L con N elementos.\n")
n=int(input("Ingrese el tamaño de la lista:\n"))
cls()
lista=[int(input(f"Ingrese el valor #{i+1}:\n")) for i in range(n)]
print(f"\nEl mayor de la lista {lista} es: {max(lista)}")