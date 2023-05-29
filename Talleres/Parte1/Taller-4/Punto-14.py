"""
El dueño de una tienda compra un artículo a 
un precio determinado. Obtener el precio en que 
lo debe vender para obtener una ganancia del 30%.
"""
#Se importa la librería OS para limpiar la pantalla 
import os

#Se importa una clase propia llamada message que formatea los mensajes
from utils import message

#Se instancia la calse message
msg = message.Message()

#Se limpia la consola
os.system('cls')

def calcular_precio(costo):
    print(msg.format_message('INFx042',costo,None,None))
    exit()

def verificar_costo(costo):
    
    if costo < 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex006',None,None,None))
    elif costo == 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex010',None,None,None))    
    else:
        calcular_precio(costo)

def main():

    print(msg.format_message('INFx041',None,None,None))

    while True:

        costo=float(input(msg.format_message('INPx017',None,None,None)))
        verificar_costo(costo)            

main()        