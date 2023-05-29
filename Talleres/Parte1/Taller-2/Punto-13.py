"""
Realice un algoritmo que, con base en un número proporcionado (1-7),
indique el día de la semana que le corresponde (L-D).
 
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
start=True
print(green+"Este algoritmo determina el dia de la semana segun su numero.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se repite si la vraiable start es verdadera
    while start:
        
        #Se capturan los datos y se guardan en las variables flotantes
        numero=int(input(blue+"Ingrese un número del 1 al 7:\n"))

        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if numero<1 or numero>7:
            os.system('cls')
            print(red+"El número debe ser entre 1 y 7.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    match numero:
        case 1: dia='Lunes'
        case 2: dia='Martes'
        case 3: dia='Miercoles'
        case 4: dia='Jueves' 
        case 5: dia='Viernes'
        case 6: dia='Sábado'
        case 7: dia='Domingo'                   
            
    
    print(green+f"Has ingresado el múmero {numero}, el dia sería {dia}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      