from package.Functions import *

"""
20.diseñar un algoritmo de una fusión que convierta una cadena en mayúscula y
otra que la convierta minúscula.
"""

def change_capital(word,opc):
    print(f"VIEJA PALABRA: {word}")
    if opc=="1": print(f"NUEVA PALABRA: {word.lower()}")
    elif opc=="2": print(f"NUEVA PALABRA: {word.upper()}")

cls()
print("Este algoritmo convierte una  letra mayuscula en minuscula y viceversa.\n")

opc=input("Ingrese 1 para Mayusculas a Minusculas.\nIngrese 2 para Minusculas a Mayusculas.\n")
cls()
word=input("Ingrese una palabra: \n")
cls()
change_capital(word,opc)
