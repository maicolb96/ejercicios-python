"""
Se les dará un bono por antigüedad a los empleados de una tienda. 
Si tienen un año, se les dará $100; si tienen 2 años, $200, y así 
sucesivamente hasta los 5 años. Para los que tengan más de 5, 
el bono será de $1000. Realice un algoritmo y represéntelo 
mediante el diagrama de flujo, el pseudocódigo y diagrama N/S 
que permita determinar el bono que recibirá un trabajador.
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
print(green+"Muestra a el valor del bono por antiguedad para un empleado de una tienda.\n")
    
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
        antiguedad=float(input(blue+"Ingrese la antiguedad en años:\n"))
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if antiguedad<=0:
            os.system('cls')
            print(red+"La antiguedad debe ser mayor a 0.")
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if antiguedad>=1 and antiguedad<2:
        bono=100
    elif antiguedad>=2 and antiguedad<=5:  
        bono=200
    elif antiguedad>5:  
        bono=1000         
    
    print(green+f"{nombre}, el bono a entregar es de ${bono} por tu antiguedad de {antiguedad} años.")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      