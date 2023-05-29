"""
Todos los lunes, miércoles y viernes, una persona corre 
la misma ruta y cronometra los tiempos obtenidos. 
Determinar el tiempo promedio que la persona tarda en 
recorrer la ruta en una semana cualquiera.
"""
#Se importa la librería OS para limpiar la pantalla 
import os

#Se importa una clase propia llamada message que formatea los mensajes
from utils import message

#Se importa la libreria numpy para manejar arreglos
import numpy as np

#Se instancia la calse message
msg = message.Message()

#Se limpia la consola
os.system('cls')

DIAS =['Lunes','Miércoles','Viernes']
tiempos=[]
error = True

def calcular_media(tiempo):
    
    global DIAS,tiempos

    #Se limpia la consola
    os.system('cls')
    
    for i in range(len(tiempos)):
        print(msg.format_message('INFx044',DIAS[i],tiempos[i],None))

    print(msg.format_message('INFx045',np.mean(tiempos),None,None))    
    exit()

def verificar_tiempo(tiempo):
    
    global error, tiempos

    if tiempo < 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex006',None,None,None))
        error=True
    elif tiempo == 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex010',None,None,None))  
        error=True  
    else:
        tiempos.append(tiempo)
        error=False

def main():
    
    global DIAS,error

    print(msg.format_message('INFx043',None,None,None))

    while True:
        for i in DIAS:
            error=True
            while error:
                tiempo=float(input(msg.format_message('INPx018',i,None,None)))
                verificar_tiempo(tiempo)
        calcular_media(tiempo)            

main()        