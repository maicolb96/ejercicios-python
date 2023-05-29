"""
Realice un algoritmo que, con base en una calificación 
proporcionada (0-10), indique con letra la calificación 
que le corresponde: 

10 es “A”, 9 es “B”, 8 es “C”, 7 y 6 son “D”, y de 5 a 0 son “F”. 
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
print(green+"Este algoritmo determina la calificación segun un valor dado.\n")
    
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
        valor_cal=int(input(blue+"Ingrese el valor de la calificación:\n"))

        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if valor_cal<0:
            os.system('cls')
            print(red+"El valor de la calificación no puede ser menor a 0.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if valor_cal == 10:
        calificacion='A'
    elif valor_cal == 9:
        calificacion='B'
    elif valor_cal == 8:
        calificacion='C'
    elif valor_cal == 6 or valor_cal == 7:
        calificacion='D' 
    elif valor_cal < 6:
        calificacion='F'           
            
    
    print(green+f"Si su valor de calificación es {valor_cal}, la calificacion sería {calificacion}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      