""" 
El teatro José de la Cruz Mena otorga descuentos según 
la edad del cliente. Determinar la cantidad de dinero 
que el teatro deja de percibir por cada una de las categorías. 
Tomar en cuenta que los niños menores de 5 años no pueden entrar 
al teatro y que existe un precio único en los asientos. 

Los descuentos se hacen tomando en cuenta el siguiente cuadro:

CATEGORIA      EDAD     DESCUENTO
Categoría 1    5-14        35%
Categoría 2    15-19       25%
Categoría 3    20-45       10%
Categoría 4    45-65       25%
Categoría 5   65 o más     35%

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

utilidad_cat1=0
utilidad_cat2=0
utilidad_cat3=0
utilidad_cat4=0
utilidad_cat5=0
error=True

#Metodo que recibe una altura y devuelve una escalera invertida de asteriscos con esa altura.
def check_value_off(edad,precio):

    global utilidad_cat1,utilidad_cat2,utilidad_cat3,utilidad_cat4,utilidad_cat5

    if edad>=5 and edad<=14:    utilidad_cat1+=precio*0.35
    elif edad>=15 and edad<=19: utilidad_cat2+=precio*0.25
    elif edad>=20 and edad<=45: utilidad_cat3+=precio*0.10
    elif edad>=46 and edad<=65: utilidad_cat4+=precio*0.25
    elif edad>=66:              utilidad_cat5+=precio*0.35

                


#Metodo que valida que el dato ingresado sea correcto.
def verify(edad,precio):

    global error

    if edad<0 or precio<0:
        print(msg.format_message('Ex006',None,None,None)+"\n")
        error=True 
    elif edad<5:
        print(msg.format_message('Ex008',None,None,None)+"\n") 
        error=True  
    else:
        error=False
        check_value_off(edad,precio)    

#Método principal
def main():
    global error
    print(msg.format_message('INFx008',None,None,None))
    while True:
        try:
            asientos=int(input(msg.format_message('INPx004',None,None,None)))
            if asientos >= 0:
                for i in range(asientos):
                    error=True 
                    while error:    
                        edad=int(input(msg.format_message('INPx005',i+1,None,None)))
                        precio=float(input(msg.format_message('INPx006',i+1,None,None)))
                        verify(edad,precio)

                print(msg.format_message('INFx009',None,None,None)+"\n") 

                utilidades=[utilidad_cat1,utilidad_cat2,utilidad_cat3,utilidad_cat4,utilidad_cat5]   
                for j in range(5):
                    print(msg.format_message('INFx010',j+1,utilidades[j],None))
                         
            else:
                print(msg.format_message('Ex006',None,None,None)+"\n")         
        except ValueError as e:
            if "int() with base 10" in str(e) or "not convert string to float" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()