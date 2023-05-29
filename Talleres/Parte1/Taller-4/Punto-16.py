"""
Tres personas deciden invertir su dinero para fundar una empresa. 
Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada quien invierte con 
respecto a la cantidad total invertida.
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

inversor =['Inversor 1','Inversor 2','Inversor 3']
inversiones=[]
error = True

def calcular_porcentaje(inversion):
    
    global inversor,inversiones

    #Se limpia la consola
    os.system('cls')
    
    print(msg.format_message('INFx047',None,None,None))
    print(msg.format_message('INFx048',np.sum(inversiones),None,None))

    for i in range(len(inversiones)):
        print(msg.format_message('INFx049',inversor[i],inversiones[i],(inversiones[i]/np.sum(inversiones))*100))
    print("\n")
    exit()

def verificar_inversion(inversion):
    
    global error, inversiones

    if inversion < 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex006',None,None,None))
        error=True
    elif inversion == 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex010',None,None,None))  
        error=True  
    else:
        inversiones.append(inversion)
        error=False

def main():
    
    global inversor,error

    print(msg.format_message('INFx046',None,None,None))

    while True:
        for i in inversor:
            error=True
            while error:
                inversion=float(input(msg.format_message('INPx019',i,None,None)))
                verificar_inversion(inversion)
        calcular_porcentaje(inversion)            

main()        