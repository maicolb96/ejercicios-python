"""
Evaluar la función y = 5X-3X +2 para cualquier valor de x. 
"""
import os

os.system("cls")
print("Este algoritmo evalua la funcion y = 5X-3X +2 para cualquier valor de x. ")

x=float(input("Ingrese el valor de X: "))

print(f"La función y = 5X-3X +2 con x={x} se evalúa asi: \n")
print(f"y = 5*({x})-3*({x})+2")
print(f"y = {5*x}-{3*x}+2")
print(f"y = {5*x-3*x+2}")