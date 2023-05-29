""" 
Leer tres números que denoten una fecha (día, mes, año). 
Comprobar que es una fecha válida. Si no es válida escribir 
un mensaje de error. Si es válida escribir la fecha cambiando 
el número del mes por su nombre. Ej. si se introduce 1 2 2006, 
se deberá imprimir “1 de febrero de 2006”. El año debe ser mayor que 0. 
(Recuerda la estructura según sea).
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

#Metodo que recibe un arreglo con 3 valores (día, mes, año) y convierte el mes a texto.
def change_date(date):
    
    #Se hace una abstracción del arreglo 
    day=date[0]; month=date[1]; year=date[2] 
    
    #Se evalúa el mes y según el número de mes se asigna el nombre del mes
    if month == 1: text_month="enero"
    elif month == 2: text_month="febrero"
    elif month == 3: text_month="marzo"
    elif month == 4: text_month="abril"
    elif month == 5: text_month="mayo"
    elif month == 6: text_month="junio"
    elif month == 7: text_month="julio"
    elif month == 8: text_month="agosto"
    elif month == 9: text_month="septiembre"
    elif month == 10: text_month="octubre"
    elif month == 11: text_month="noviembre"
    elif month == 12: text_month="diciembre"
    
    #Imprime la fecha en el formato: N de mes del NNNN
    print(msg.format_message('INFx002',day,text_month,year))


#Metodo que se encarga de verificar que la fecha este correcta
def validate_date(date):

    error=False
    day=date[0]; month=date[1]; year=date[2]
 
    if day>31 or day < 1:
        print(msg.format_message('Ex001',None,None,None))
        error=True
    if month > 12 or month < 1:
        print(msg.format_message('Ex002',None,None,None))
        error=True
    if len(str(year))!=4:
        print(msg.format_message('Ex003',None,None,None))  
        error=True   

    if error:
        print('\n') 
        os.system('pause')
        os.system('cls')
        print(msg.format_message('Ex004',None,None,None)+"\n")
    else: 
        change_date(date);exit()
    


#Método principal
def main():
    print(msg.format_message('INFx001',None,None,None))
    fecha_texto=["día","mes","año"]

    while True:
        
        date=[]
        try: 
            for fecha in fecha_texto: 
                date.append(int(input(msg.format_message('INPx001',fecha,None,None))))
            print('\n')
            validate_date(date)    
        except ValueError as e:
            if "int() with base 10" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")
main()