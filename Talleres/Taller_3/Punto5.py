from package.Functions import *
import Punto1 as p1

"""
5.	Crea una lista llamada sublista que contenga los elementos del índice 2 al 4 de la lista números.
"""

cls()
sublista = [p1.numeros[i] for i in range(2,5,1)]
print("Este algoritmo a crea una lista llamada sublista que contenga los elementos del índice 2 al 4 de la lista números.")
print(sublista)