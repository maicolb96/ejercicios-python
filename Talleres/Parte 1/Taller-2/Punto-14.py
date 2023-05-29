"""
El secretario de educación ha decidido otorgar un bono 
por desempeño a todos los profesores con base 
en la puntuación siguiente:

    Puntos              Premio
0 - 100              1 salario   
101 - 150            2 salarios mínimos  
151 - en adelante    3 salarios mínimos 
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
print(green+"Determina un bono por desempeño para los profesores.\n")
    
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
        puntos=int(input(blue+"Ingrese el puntaje obtenido:\n"))
        salario=float(input(blue+"Ingrese el salario mínimo:\n"))

        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if puntos<0:
            os.system('cls')
            print(red+"Los puntos deben ser mayores o iguales a 0.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if puntos >=0 and puntos <=100: bono=salario
    elif puntos >=101 and puntos <=150: bono=salario*2
    elif puntos >=151: bono=salario*3
             
            
    
    print(green+f"Como has obtenido un puntaje de {puntos} puntos, has ganado un bono de ${bono}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      