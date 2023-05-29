"""
Este programa es un ejemplo del case en python
comienza con un match luego bariable y luego casos
"""

#Importando libreria os que permita interactuar con el sistema operativo
import os

#Usando el metodo system de la clase os para limpiar la pantalla
os.system('cls')

#Se guarda en la variable un número del 1 al 10
var=input("Ingrese un número del 1 al 10: \n")

#Evalua segun la variable que contiene el número
#Se crea un caso para cada número y se ejecuta un print
match var:
    case '1':
        print("Animal 1")
    case '2':
        print("Animal 2")  
    case '3':
        print("Animal 3") 
    case '4':
        print("Animal 4") 
    case '5':
        print("Animal 5")
        