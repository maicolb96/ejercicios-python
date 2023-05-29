"""
Evaluar la función y = 3x^2+2x-5 para 
cualquier valor de x. (caso normal)
"""
import os
os.system("cls")

print("Este algoritmo evalua la función y = 3x^2 + 2x -5 para x.\n")

x=float(input("Ingrese el valor de x: "))

print(f"La función y = 3x^2 + 2x - 5 con x={x} se evalúa asi: \n")
print(f"y = 3*({x}^2)+2*({x})-5")
print(f"y = 3*{x**2}+{2*x}-5")
print(f"y = {(3*(x**2))+2*x-5}")