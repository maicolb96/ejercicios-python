"""
Se requiere un algoritmo para determinar, de N cantidades, 
cuántas son cero, cuántas son menores a cero, y cuántas son mayores a cero.
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
print(green+"Determina el cuantas cantidades son cero, menores a cero y mayores a cero.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    cantidad = int(input(blue+"Ingrese la cantidad de números a ingresar: \n"))
    menores=0; iguales=0; mayores=0

    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    for i in range(cantidad):

        num=float(input(f"Ingrese el {i+1}º número: "))

        if num<0:menores+=1
        elif num==0:iguales+=1
        else:mayores+=1
    
    print(green+f"\nNúmeros menores que 0: {menores}")
    print(green+f"Números iguales que 0: {iguales}")
    print(green+f"Números mayores que 0: {mayores}")

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      