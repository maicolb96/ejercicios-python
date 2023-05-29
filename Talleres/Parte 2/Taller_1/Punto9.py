from package.Functions import *

"""
Escribir una función booleana Digito que determine si 
un carácter es uno de los dígitos 0 al 9.
"""

def verifyNum(text):
    cont=0
    for i in range(10):
        if str(i) in text: 
            print(f"El número {i} se encuentra en el texto ingresado.")
            cont+=1
    if cont==0:print("En el texto ingresado no hay ningún número del 0 al 9.")

cls()

print("Este programa recibe un texto e indica si hay un número del 0 al 9.\n")
verifyNum(input("Ingrese un texto: \n"))
