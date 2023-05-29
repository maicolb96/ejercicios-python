"""
Un cliente de un banco deposita X cantidad de pesos 
cada mes en una cuenta de ahorros. La cuenta percibe 
un interés fijo durante un año de 10 % anual. Realice 
un algoritmo para determinar el total de la inversión 
final de cada año en los próximos N años.
"""
#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color

#Utiliza la función system para limpiar la consola
os.system('cls')

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#Inicializa la variable start en verdader
print(green+"Este algoritmo determina el total de la inversión final de cada año en los próximos N años.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    cantidad = int(input(blue+"Ingrese la cantidad de años que ahorro su dinero: \n"))
    i=0; años=0; monto_ahorrado=0; total_ahorrado=0
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    while años<cantidad:
        
        monto=float(input(f"Ingrese el monto a ingresar el mes {i+1}: "))
        monto_ahorrado=monto_ahorrado+monto
        i+=1
        if i%12==0:
            print(green+f"\nEl monto ahorrado el año {años} es de ${monto_ahorrado} y el interes es de ${monto_ahorrado*0.10} para un total de ${monto_ahorrado+(monto_ahorrado*0.10)}\n")
            total_ahorrado=total_ahorrado+monto_ahorrado
            monto_ahorrado=0
            años=años+1
            i=0
            
     
    print(green+f"\nEl monto total ahorrado es de ${total_ahorrado} y el interes es de ${total_ahorrado*0.10} para un total de ${total_ahorrado+(total_ahorrado*0.10)}\n")    

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      

      

      