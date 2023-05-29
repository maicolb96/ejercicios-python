""" 
Algoritmo que dado un año, nos diga si es bisiesto o no. 
Un año es bisiesto bajo las siguientes condiciones:

- Un año divisible por 4 es bisiesto y no debe ser divisible entre 100.
- Si un año es divisible entre 100 y además es divisible entre 400, 
también resulta bisiesto.

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
def check_leap_year(year):
    
    print("\n")
    if year%4==0 and year%100!=0:
        print(msg.format_message('INFx006',year,None,None))
    elif year%100==0 and year%400==0:
        print(msg.format_message('INFx006',year,None,None))
    else:
        print(msg.format_message('INFx007',year,None,None))        
    print("\n")
    exit()

#Metodo que valida que el dato ingresado sea correcto.
def verify(year):
    if year<0:
        print(msg.format_message('Ex006',None,None,None)+"\n") 
    elif len(str(year))!=4:
        print(msg.format_message('Ex003',None,None,None)+"\n")   
    else:
        check_leap_year(year)    

#Método principal
def main():
    
    print(msg.format_message('INFx005',None,None,None))
    while True:
        try:
            año=int(input(msg.format_message('INPx003',None,None,None)))
            verify(año)     
        except ValueError as e:
            if "int() with base 10" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()