"""
Realice un algoritmo que permita determinar el sueldo semanal
de un trabajador con base en las horas trabajadas y el pago por hora,
considerando que a partir de la hora número 41 y hasta la 45,
cada hora se le paga el doble, de la hora 46 a la 50, el triple,
y que trabajar más de 50 horas no está permitido.
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
print(green+"Este algoritmo permite determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se asignan los valores capturados por consola a las variables correspondientes
    nombre=input(blue+"Ingrese el nombre del empleado:\n")
    
    #Se repite si la vraiable start es verdadera
    while start:
        
        #Se capturan los datos y se guardan en las variables flotantes
        horas_trabajadas=float(input(blue+"Ingrese la cantidad de horas trabajadas:\n"))
        valor_hora=float(input(blue+"Ingrese el valor por hora:\n"))
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if horas_trabajadas<=0 or valor_hora<=0:
            os.system('cls')
            print(red+f"{nombre}, las horas trabajadas y el valor por hora debe ser mayor a 0.")
        elif horas_trabajadas > 50:
            os.system('cls')
            print(red+f"{nombre}, las horas trabajadas nunca pueden superar las 50.")    
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if horas_trabajadas < 41:
        sueldo=horas_trabajadas*valor_hora
    elif horas_trabajadas >= 41 and horas_trabajadas <= 45:
        sueldo=horas_trabajadas*(valor_hora*2)     
    elif horas_trabajadas >= 46 and horas_trabajadas <= 50:
        sueldo=horas_trabajadas*(valor_hora*3)            
    
    print(green+f"{nombre}, total a pagar por {horas_trabajadas} horas de trabajo es de: ${sueldo}.")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      