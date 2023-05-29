from package.Functions import *

"""
Realizar un procedimiento que obtenga la división 
entera y el resto de la misma utilizando la únicamente 
los operadores suma y resta
"""

def division(dividendo,divisor):
    cont=0
    while True:
        dividendo-=divisor
        if dividendo<0: break
        else: residuo = dividendo
        cont+=1
    return (cont,residuo)

cls()
print("Este programa calcula el resultado y residuo de una división.\n")
dividendo=float(input("Ingrese el dividendo: \n"))
divisor=float(input("Ingrese el divisor: \n"))
print(f"\nCociente: {division(dividendo,divisor)[0]}")
print(f"Residuo: {division(dividendo,divisor)[1]}")


