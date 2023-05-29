"""
En un hospital existen tres áreas: 
Ginecología, Pediatría, Traumatología. 
El presupuesto anual del hospital se reparte 
conforme a la sig. Tabla:

    Área       | Porcentaje Ppto
---------------|-----------------
 Ginecología   |      40%
Traumatología  |      30%
  Pediatría    |      30%

Obtener la cantidad de dinero que recibirá cada área, 
para cualquier monto presupuestal.  
"""
#Se importa la libreria os para manipular el sistema operativo
import os

#Se importa una clase propia mensajes que da formato a los mensaje
from utils import message

#Se instancia la clase Message
msg = message.Message()

#Se limpia la consola
os.system('cls')

#Funcion que calcula el presupuesto para cada area recibiendo un parametro
def calcular_cant(monto):

    #Se limpia la consola
    os.system('cls')

    #Se imprime la información
    print(msg.format_message('INFx037',monto,None,None))
    print(msg.format_message('INFx038',monto,None,None))
    print(msg.format_message('INFx039',monto,None,None))
    print(msg.format_message('INFx040',monto,None,None))
    print("\n")

    #Se finaliza la ejecución del programa
    exit()

#Funcion que verifica si el monto ingresado es correcto
def verificar_monto(monto):

    if monto < 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex006',None,None,None))
    elif monto == 0:
        #Se limpia la consola
        os.system('cls')
        print(msg.format_message('Ex010',None,None,None))
    else:
        #Si el monto es correcto, se llama la función calcular cant
        calcular_cant(monto)   

#Metodo principal recoge la información inicial para operar
def main():

    print(msg.format_message('INFx036',None,None,None))
    
    #Se repite mientras verificar_monto determine que el monto no es valido
    while True:
        monto=float(input(msg.format_message('INPx016',None,None,None)))
        verificar_monto(monto)

main()
