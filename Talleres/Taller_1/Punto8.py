from package.Functions import *

"""
Escribir una función Salario que calcula los 
salarios de un trabajados para un numero dado 
de horas trabajadas y un salario hora. Las horas 
que superan las 40 horas semanales se pagaran como 
extras con un salario hora 1,5 veces el salario ordinario.
"""

def calculatePay(h,vh):
    pay = h*vh if h<=40 else (40*vh)+((h-40)*(vh*1.5))
    return pay

cls()
print("Este programa calcula el salario según las horas trabajadas y su valor.\n")
h=float(input("Ingrese las horas trabajadas: \n"))
vh=int(input("Ingrese el valor en pesos de la hora trabajada: \n"))
print(f"El saldo a pagar es de ${calculatePay(h,vh)}")