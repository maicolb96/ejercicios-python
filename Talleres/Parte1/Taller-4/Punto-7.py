""" 
Determinar la cantidad semanal de dinero que recibirá 
cada uno de los n obreros de una empresa. Se sabe que 
cuando las horas que trabajo un obrero exceden de 40, 
el resto se convierte en horas extras que se pagan al 
doble de una hora normal, cuando no exceden de 8; cuando 
las horas extras exceden de 8 se pagan las primeras 8 al 
doble de lo que se paga por una hora normal y el resto al triple.
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

error=True
info = []
#Metodo que recibe una altura y devuelve una escalera invertida de asteriscos con esa altura.
def check_pay(nombre,horas_trabajadas,valor_hora):

    global info
    pago_simple=0
    pago_doble=0
    pago_triple=0
    horas_simples=0
    horas_extra=horas_trabajadas-40

    if horas_trabajadas > 40:
        horas_simples=40
        pago_simple=40*valor_hora
        if horas_extra > 8:
            pago_doble=8*(valor_hora*2)
            pago_triple=((horas_extra)-8)*(valor_hora*3)
        else:
            pago_doble=(horas_extra)*(valor_hora*2)
            pago_triple=0
    else:
        horas_simples=horas_trabajadas
        horas_extra=0
        pago_doble=0
        pago_triple=0
        pago_simple=horas_trabajadas*valor_hora  
    
    total_pago=pago_simple+pago_doble+pago_triple
            
    info.append([
        f"Nombre: {nombre}",
        f"Valor por hora: ${valor_hora}",
        f"Horas totales trabajadas: {horas_trabajadas}",
        f"Horas normales trabajadas: {horas_simples}",
        f"Horas extra trabajadas: {horas_extra}",
        f"Pago por horas simples: ${pago_simple}",
        f"Pago por horas extra: ${pago_doble+pago_triple}",
        f"Total a pagar: ${total_pago}"
    ])
    
    

#Metodo que valida que el dato ingresado sea correcto.
def verify(nombre,horas_trabajadas,valor_hora):

    global error

    if horas_trabajadas<0 or valor_hora<0:
        print(msg.format_message('Ex006',None,None,None)+"\n")
        error=True  
    else:
        error=False
        check_pay(nombre,horas_trabajadas,valor_hora)

#Metodo que imprime los datos a partir de un arreglo
def print_pay():
    global info

    for i in info:
        print(msg.format_message('INFx017',info.index(i),None,None)) 
        for j in range(len(i)):
            print(i[j])
        print("\n")    
    
    exit()         

#Método principal
def main():
    
    global error, info

    print(msg.format_message('INFx016',None,None,None))
    while True:
        try:
            cant_obreros=int(input(msg.format_message('INPx008',None,None,None)))
            os.system('cls')
            if cant_obreros >= 0:
                for i in range(cant_obreros):
                    error=True 
                    while error:
                        nombre=input(msg.format_message('INPx009',i+1,None,None))    
                        horas_trabajadas=int(input(msg.format_message('INPx010',nombre,None,None)))
                        valor_hora=float(input(msg.format_message('INPx011',nombre,None,None)))
                        print("\n")
                        verify(nombre,horas_trabajadas,valor_hora)
                
                os.system('cls')
                print(msg.format_message('INFx018',None,None,None)+"\n")             
            else:
                print(msg.format_message('Ex006',None,None,None)+"\n")

            print_pay()          
        except ValueError as e:
            if "int() with base 10" in str(e) or "not convert string to float" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()