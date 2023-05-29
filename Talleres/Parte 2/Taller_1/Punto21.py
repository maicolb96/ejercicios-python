from package.Functions import *

"""
21.disear una función que informa si una cadena 
es palíndromo (una cadena es palíndromo si se lee 
igual de izquierda a derecha que de derecha a izquierda).
"""

def is_palindromo(cadena):
    cadena_inversa=""
    for i in range(0,len(cadena),1):
       cadena_inversa+=cadena[len(cadena)-1:]
       cadena = cadena[:-1]
    return cadena_inversa

cls()
print("Este algoritmo verifica si una palabra es palíndromo.\n")
palabra=input("Ingrese una palabra: \n").upper()
inversa=is_palindromo(palabra).upper()
cls()
print(f"PALABRA ORIGINAL: {palabra}\nPALABRA INVERSA: {inversa}")
if palabra==inversa: print(f"\nLa palabra ({palabra}) es palíndromo.")
else: print(f"\nLa palabra ({palabra}) no es palíndromo.")

