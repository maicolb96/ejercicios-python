"""
Evaluar la función y = -5x^3 - 3x^2 + 8 
para cuando x vale 4. (No ocupa entradas)
"""

import os
os.system("cls")

print("Este algoritmo evaluar la función y = -5x^3 - 3x^2 + 8 para cuando x vale 4.\n")

x=4

print(f"La función y = -5x^3 - 3x^2 + 8 con x={x} se evalúa asi: \n")
print(f"y = -5*({x}^3)-3*({x}^2)+8")
print(f"y = -5*{x**3}-3*{x**2}+8")
print(f"y = {(-5*(x**3))-3*(x**2)+8}")