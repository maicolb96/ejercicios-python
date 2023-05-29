from package.Functions import *

"""
Diseñar una función que calcule X ́n para X, 
variable real y n variable entera.
"""

#Función que calcula una potencia a partir de dos parametros (base,exponente)
def potencia():
    return x**n

#Se limpia la consola
cls()

#Se indica que hace el programa
print("Este programa calcula la potencia de una base real con exponente entero.\n")

#Se leen los valores de la base y exponente
x=float(input("Ingrese la base de la potencia: \n"))
n=int(input("Ingrese el exponente de la potencia: \n"))

#Se imprime el retorno de la función potencia
print(f"La potencia de {x} elevado a {n} es: {potencia()}")


