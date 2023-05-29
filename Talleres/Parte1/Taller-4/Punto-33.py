"""
Dado un número(N) cualesquiera obtener su raíz y potencia cuadrada.
"""

import os,math

os.system("cls")

print("Este algoritmo, dado un número(N) cualesquiera obtiene su raíz y potencia cuadrada.\n")

num=float(input("Ingrese un número: "))
print(f"\nLa potencia cuadrada de {num} es: {num**2}\n"
      f"La raiz cuadrada de {num} es: {math.sqrt(num)}")