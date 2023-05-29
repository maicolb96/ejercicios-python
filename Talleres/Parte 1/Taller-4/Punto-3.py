""" 
Algoritmo que lea un número entero (altura) y a partir 
de él cree una escalera invertida de asteriscos con esa altura. 
Deberá quedar así, si ponemos una altura de 5.

*****
 ****
  ***
   **
    *

"""
#Se importa la librería OS que permite interactuar con el sistem
import os
#Se importa un controlador de mensajes creado por mi
from utils import message 

#Se limpia la consola
os.system('cls')   

#Se instancia la clase Message y se crea un objeto llamado msg
msg = message.Message()

"""Nota, msg permite acceder al metodo format_message de la clase Message
   El cual se encarga de retornar un mensaje estructurado según el código
   Que recibe, además puede recibir hasta 3 argumentos para ser usados
   Como variables concatenadas en el texto.
"""

#Metodo que recibe una altura y devuelve una escalera invertida de asteriscos con esa altura.
def make_figure(lado):
    
    print("\n")
    for i in range(lado):
        print(" "*i + "*"*(lado-i))
    print("\n")
    exit()

#Metodo que valida que el dato ingresado sea correcto.
def verify(lado):
    if lado>1:
        make_figure(lado)
    elif lado<0:
        print(msg.format_message('Ex006',None,None,None)+"\n")
    else:
        print(msg.format_message('Ex007',None,None,None)+"\n")

#Método principal
def main():
    
    print(msg.format_message('INFx004',None,None,None))
    while True:
        try:
            lado=int(input(msg.format_message('INPx002',None,None,None)))
            verify(lado)     
        except ValueError as e:
            if "int() with base 10" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()