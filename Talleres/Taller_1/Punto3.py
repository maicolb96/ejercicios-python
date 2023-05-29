from package.Functions import *
import numpy as np

"""
Diseñar el algoritmo para calcular el máximo común 
divisor de cuatro números basado en una su algoritmo 
función mcd(el máximo común divisor de dos números).
"""

#Función que calcula el MCD de tres números, recive un vector de dimensión 3
#y retorna el MCD de los 3 números.
def mcd(n):
    res = [i for i in range(1,np.min(n)+1,1) if n[0]%i==0 and n[1]%i==0 and n[2]%i==0]
    return res

#Se limpia la pantalla
cls()

#Se explica que hace el programa
print("Este algoritmo calcula el Máximo Común Divisor de 3 números.\n")

#Se leen 3 números usando la Comprensión de listas y se almacenan en un vector
vector=[int(input(f"Ingrese el número #{i}: \n")) for i in range(1,4,1)]

#Se llama la función mcd y a su retorno se le aplica la función max de numpy
mcd=np.max(mcd(vector))

#Se imprime el resultado
print(f"\nEl MCD de {vector[0]},{vector[1]} y {vector[2]} es: {mcd}")

