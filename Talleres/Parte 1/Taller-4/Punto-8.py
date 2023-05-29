""" 
Leer los 2500 votos otorgados a los 3 candidatos a 
alcalde de la ciudad de León e imprimir el número del 
candidato ganador y su cantidad de votos.
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
info=[]
#Metodo que recibe una altura y devuelve una escalera invertida de asteriscos con esa altura.
def save_data(cantidad_votos,candidato):

    global info
    info.append([cantidad_votos,candidato])
      
def check_winner():
     
    mayor=0
    ganador=0

    if info[0][0] > info[1][0] and info[0][0] > info[2][0]:
        mayor=info[0][0]
        ganador=info[0][1]
    elif info[1][0] > info[0][0] and info[1][0] > info[2][0]:
        mayor=info[1][0]
        ganador=info[1][1]
    elif info[2][0] > info[0][0] and info[2][0] > info[1][0]:
        mayor=info[2][0]
        ganador=info[2][1]
    
    os.system('cls')
    print(msg.format_message('INFx020',mayor,ganador,None))                    
            
         
         


#Metodo que valida que el dato ingresado sea correcto.
def verify(numero_votos,candidato):

    global error

    if numero_votos<0:
        print(msg.format_message('Ex006',None,None,None)+"\n")
        error=True  
    else:
        error=False
        save_data(numero_votos,candidato)        

#Método principal
def main():
    
    global error, info
    winner = []
    print(msg.format_message('INFx019',None,None,None))
    while True:
        try:
            for i in range(3):
                error=True 
                while error:
                    numero_votos=int(input(msg.format_message('INPx012',i+1,None,None)))
                    print("\n")
                    verify(numero_votos,i+1)
            check_winner()
        except ValueError as e:
            if "int() with base 10" in str(e):
                print(msg.format_message('Ex005',None,None,None)+"\n")  
main()