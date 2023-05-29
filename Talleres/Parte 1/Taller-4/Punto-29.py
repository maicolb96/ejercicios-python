"""
Evaluar el factorial de cualquier 
numero usando la fórmula: n!=n!-1
"""
import os
import math
os.system("cls")

print("Este algoritmo valua el factorial de cualquier numero usando la fórmula: n!=n!-1\n")

num=int(input("Ingrese un número: "))
print(f"El factorial de {num} es {num*math.factorial(num-1)}")