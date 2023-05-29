"""
Calcular el área de un circulo con la formula:
area = PI * RADIO**2
"""
import os, math

os.system("cls")

print("Este algoritmo calcula el área de un circulo.\n")

radio=float(input("Ingrese el radio del circulo: "))

print(f"El área del circulo es: {math.pi*(radio**2):.2f} unidades cuadradas.")