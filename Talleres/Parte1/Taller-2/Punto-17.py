"""
Realice un algoritmo que permita determinar la cantidad del bono 
navideño que recibirá un empleado de una tienda, considerando que 
si su antigüedad es mayor a cuatro años o su sueldo es menor de dos 
mil pesos, le corresponderá 25 % de su sueldo, y en caso contrario 
sólo le corresponderá 20 % de éste.
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
print(green+"Determina el bono segun la antiguedad.\n")
    
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
        antiguedad=float(input(blue+"Ingrese la antiguedad:\n"))
        sueldo=float(input(blue+"Ingrese el sueldo:\n"))
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if antiguedad<0 or sueldo<0:
            os.system('cls')
            print(red+"El sueldo o la antiguedad no puede ser menor a cero.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if antiguedad > 4 or sueldo < 2000: 
        bono=0.25*sueldo
    else:
        bono=0.20*sueldo

             
            
    
    print(green+f"Como tu sueldo es de ${sueldo} y la antiguedad es de {antiguedad} años, el bono es de ${bono}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      