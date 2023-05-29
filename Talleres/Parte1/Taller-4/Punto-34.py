"""
Determinar la media de una lista indefinida 
de números positivos, terminados con un 
número negativo.
"""
import os
import numpy as np

os.system("cls")
print("Este algortimo determinar la media de una lista indefinida\n" 
      "de números positivos, terminados con un número negativo.\n")

tamaño=int(input("Ingrese el tamaño de la lista: "))
array=[]

for i in range(tamaño):
    num=float(input(f"Ingrese el número #{i+1}: "))
    if i!=tamaño-1: array.append(num)
    else: array.append(-num)  
os.system("cls")
print(f"El arreglo de números es: {array}\n"
      f"La media de los números del arreglo es: {np.mean(array)}")  
