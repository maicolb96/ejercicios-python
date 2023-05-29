"""
Los directivos de equis escuela requieren determinar cuál es la edad
 promedio de cada uno de los M salones y cuál es la edad promedio de 
 toda la escuela. Realice un algoritmo para determinar estos promedios.
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
print(green+"Este algoritmo determina cuál es la edad promedio de cada uno de los M salones y cuál es la edad promedio de toda la escuela.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    salones = int(input(blue+"Ingrese la cantidad de salones: \n"))
    i=0; j=0; sum_edad=0; promedio_escuela=0
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    for i in range(salones):
        sum_edad=0 
        estudiantes=int(input(blue+f"Ingrese la cantidad de estudiantes del salon {i+1}:\n"))
        for j in range(estudiantes):
            edad=int(input(blue+f"Ingrese la edad del estudiante {j+1}:\n"))
            sum_edad=sum_edad+edad
        print(green+f"\nEl promedio de edad del salon {salones} es:{sum_edad/estudiantes}\n") 
        promedio_escuela=promedio_escuela+(sum_edad/estudiantes)
        
    print(green+f"El promedio de edad de la escuela es:{promedio_escuela/salones}\n")    

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      

      

      