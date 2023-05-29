from package.Functions import *

"""
10.Diseñar una función que permita devolver 
el valor absoluto de un numero.
"""

def absolute(n):
    return abs(n) 

cls()
print("Este programa devuelve el valor absoluto de un número.\n")
n=float(input("Ingrese un número: \n"))
print(f"El valor absoluto de {n} es {absolute(n)}.")