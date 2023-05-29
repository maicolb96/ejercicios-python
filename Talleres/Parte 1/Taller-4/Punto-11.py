""" 
Calcular el nuevo salario de un obrero si obtuvo un 
incremento del 25% sobre su salario anterior.
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
# Inicializar las variables contadoras y acumuladores


def calculate_new_pay(salario_anterior):
    print(msg.format_message('INFx035',salario_anterior,None,None))
    exit()
   
def verify_salario(salario_anterior):
    
    if salario_anterior < 0:
        #Se limpia la consola
        os.system('cls') 
        print(msg.format_message('Ex006',None,None,None))
    elif salario_anterior == 0:
        #Se limpia la consola
        os.system('cls') 
        print(msg.format_message('Ex010',None,None,None))
    else:
        calculate_new_pay(salario_anterior)

def main():

    #Mensaje que dice de que es el algoritmo
    print(msg.format_message('INFx034',None,None,None))
    
    while True:

        salario_anterior = float(input(msg.format_message('INPx015',None,None,None)))
        verify_salario(salario_anterior)

main()

                

