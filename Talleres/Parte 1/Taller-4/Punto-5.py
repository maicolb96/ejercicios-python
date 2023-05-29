""" 
En una tienda de descuento las personas que van a 
pagar el importe de su compra llegan a la caja y sacan 
una bolita de color, que les dirá que descuento tendrán 
sobre el total de su compra. Determinar la cantidad que 
pagara cada cliente desde que la tienda abre hasta que cierra. 
Se sabe que si el color de la bolita es roja el cliente obtendrá 
un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá 
descuento.
"""
#Se importa la librería OS que permite interactuar con el sistem
import os
#Se importa un controlador de mensajes creado por mi
from utils import message 
#Se importa la libreria random para usar su funcion choice
import random as rm
#Se importa para poder realizar una espera en la ejecución utilizando la función sleep
import time
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
def check_value_off(importe):

    colors = ["Roja","Amarilla","Blanca"]
    selected = rm.choice(colors)
    descuento=0

    print(msg.format_message('INFx011',selected,None,None)+"\n")
    time.sleep(4)

    if selected=="Roja":
        descuento=importe*0.40
        print(msg.format_message('INFx012',selected,"40%",None)+"\n")
    elif selected=="Amarilla":
        descuento=importe*0.25 
        print(msg.format_message('INFx012',selected,"25%",None)+"\n")
    elif selected=="Blanca":
        descuento=importe*0
        print(msg.format_message('INFx013',selected,None,None)+"\n") 

    print(msg.format_message('INFx014',importe,descuento,None)+"\n")
    exit()   

#Metodo que valida que el dato ingresado sea correcto.
def verify(importe):

    if importe<0:
        print(msg.format_message('Ex006',None,None,None)+"\n")
    elif importe==0:
        print(msg.format_message('Ex009',None,None,None)+"\n")  
    else:
        check_value_off(importe)    

#Método principal
def main():
    global error
    print(msg.format_message('INFx015',None,None,None))
    while True:
        try:
            importe=float(input(msg.format_message('INPx007',None,None,None)))
            verify(importe)       
        except ValueError as e:
            if "not convert string to float" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()