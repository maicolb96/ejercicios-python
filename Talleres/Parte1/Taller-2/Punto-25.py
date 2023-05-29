"""
Se requiere un algoritmo para determinar cuánto ahorrará
en pesos una persona diariamente, y en un año, si ahorra 3¢ 
el primero de enero, 9¢ el dos de enero, 27¢ el 3 de enero 
y así sucesivamente todo el año.
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
print(green+"Este algoritmo determina cuánto ahorrará en pesos una persona diariamente, y en un año, si ahorra 3¢ el primero de enero, 9¢ el dos de enero, 27¢ el 3 de enero y así sucesivamente todo el año.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    ahorro_inicial=3
   
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    for i in range(365):
        if i>0:
            ahorro_inicial=ahorro_inicial*3
        print(f"El ahorro del día {i+1} es de {ahorro_inicial}")
    
    print(f"\nEl ahorro total en el año es de {ahorro_inicial}")

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      