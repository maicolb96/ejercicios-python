""" 
El dueño de un estacionamiento requiere un algoritmo que 
le permita determinar cuánto debe cobrar por el uso del 
estacionamiento a sus clientes. Las tarifas que se tienen 
son las siguientes:
 
Las dos primeras horas a $5.00 c/u. 
Las siguientes tres a $4.00 c/u. 
Las cinco siguientes a $3.00 c/u. 

Después de diez horas el costo por cada una es de dos pesos.
"""


#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color

#Utiliza la función system para limpiar la consola
os.system('cls')

#Inicializa la variable start en verdader
start=True
print("Este algoritmo determina el cobro por el uso de un estacionamiento.\n")

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#El ciclo se ejecuta mientras start sea verdadero
while start:
    
    """
    Try
    Verifica si hay errores en la ejecución, en try se ejecuta
    el código sin errores.
    Except
    En except se ejecuta el código cuando hay un error.
    """
    try:
        horas=float(input(blue+"Ingrese la cantidad de horas en el estacionamiento: \n"))
       
        #Se verifica si los datos ingresados son negativos
        if horas<0:
            os.system('cls')
            print(red+"La horas no pueden ser menores a 0.\n")
        else:
            #Si los datos son positivos cambia el estado de start y sale del ciclo
            start=False 
    except:
        os.system('cls')
        print(red+"Ha ocurrido un error, vuelva a ingresar los datos.\n")
      

#Define que puede comprar según el valor de la variable cash y lo imprime
if horas==0:
    print(red+f"\nNo debes nada, no se quedo en el estacionamiento.\n")
elif horas<=2:
    print(green+f"\nEstuviste {horas} horas, debes pagar ${5*horas}\n")
elif horas<=5 and horas>2:
    print(green+f"\nEstuviste {horas} horas, debes pagar ${4*horas}\n")
elif horas<=10 and horas>5:
    print(green+f"\nEstuviste {horas} horas, debes pagar ${3*horas}\n")
elif horas>10:
    print(green+f"\nEstuviste {horas} horas, debes pagar ${2*horas}\n")
    
    
        
   