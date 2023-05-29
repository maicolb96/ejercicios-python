"""
Una compañía fabrica focos de colores (verdes, blancos y rojos). 
Se desea contabilizar, de un lote de N focos, el número de focos 
de cada color que hay en existencia.
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
print(green+"Este algoritmo contabiliza, de un lote de N focos, el número de focos de cada color que hay en existencia.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    cantidad = int(input(blue+"Ingrese la cantidad de focos a ingresar: \n"))
    verdes=0; blancos=0; rojos=0

    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    for i in range(cantidad):

        color=input(f"Ingrese el color del {i+1}º foco: ")

        if color=="verde" or color=="Verde":verdes+=1
        elif color=="blanco" or color=="Blanco":blancos+=1
        elif color=="rojo" or color=="Rojo":rojos+=1
        else:print("Color de foco no existe.");exit()
    
    print(green+f"\nFocos Blancos: {blancos}")
    print(green+f"Focos Verdes: {verdes}")
    print(green+f"Focos Rojos: {rojos}")

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      