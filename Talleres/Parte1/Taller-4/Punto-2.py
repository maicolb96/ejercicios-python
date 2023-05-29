""" 
Algoritmo que lea un número entero (lado) y a partir de él 
cree un cuadrado de asteriscos con ese tamaño. Los asteriscos 
sólo se verán en el borde del cuadrado, no en el interior. 
Ejemplo, para lado = 4 escribiría:

****
*  * 
*  * 
****

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

#Metodo que recibe un entero y devuelve un cuadrado de lado igual al entero recibido.
def make_figure(lado):
    
    print("\n")
    for x in range(lado):
        new_matriz=''
        for y in range(lado):
            if x == 0 or x == lado-1 or y==0 or y==lado-1:
                new_matriz = new_matriz + '*  '
            else:
                new_matriz = new_matriz + '   '         
        print(new_matriz)
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

    print(msg.format_message('INFx003',None,None,None))
    while True:
        try:
            lado=int(input(msg.format_message('INPx002',None,None,None)))
            verify(lado)     
        except ValueError as e:
            if "int() with base 10" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()