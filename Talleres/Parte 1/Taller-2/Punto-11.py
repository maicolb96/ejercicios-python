"""
Los alumnos de una escuela desean realizar un viaje de estudios, 
pero requieren determinar cuánto les costará el pasaje, 
considerando que las tarifas del autobús son las siguientes: 

si son más de 100 alumnos, el costo es de $20; 
si son entre 50 y 100, $35; entre 20 y 49, $40, 
y si son menos de 20 alumnos, $70 por cada uno. 
Realice el algoritmo para determinar el costo del 
pasaje de cada alumno.
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
print(green+"Este algoritmo determina el costo de un paseo escolar.\n")
    
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
        cant_alumnos=int(input(blue+"Ingrese la cantidad de alumnos que asistirán:\n"))

        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if cant_alumnos<=0:
            os.system('cls')
            print(red+"Las cantidad de alumnos debe ser mayor a 0.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if cant_alumnos <20:
        costo=70
    elif cant_alumnos >= 20 and cant_alumnos <= 49:
        costo=40
    elif cant_alumnos >= 50 and cant_alumnos <= 100:
        costo=35
    elif cant_alumnos > 100:
        costo=20        
            
    
    print(green+f"Al ser {cant_alumnos} estudiantes, el costo de transporte para el paseo escolar es de: ${costo*cant_alumnos}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      