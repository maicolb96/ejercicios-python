"""
Determinar la media de 5 números diferentes.
"""

import os
os.system("cls")

print("Este algoritmo determina la media de 5 números diferentes.\n")
suma=0

for i in range(5):
    num=float(input(f"Ingrese el número #{i+1}: "))
    suma+=num

print(f"\nLa media de los números ingresados es de: {suma/5}")