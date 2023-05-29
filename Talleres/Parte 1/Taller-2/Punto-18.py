"""
La secretaria de salud requiere un algoritmo que permita determinar 
qué tipo de vacuna (A, B o C) debe aplicar a una persona, considerando 
que si es mayor de 70 años, sin importar el sexo, se le aplica la tipo C; 
si tiene entre 16 y 69 años, y es mujer, se le aplica la B, y si es hombre, 
la A; si es menor de 16 años, se le aplica la tipo A, sin importar el sexo.
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
print(green+"Determina que tipo de vacuna debe aplicarse a una persona.\n")
    
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
        edad=int(input(blue+"Ingrese la edad:\n"))
        sexo=input(blue+"Ingrese el sexo hombre o mujer:\n")
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if edad<0 or edad<0:
            os.system('cls')
            print(red+"La edad no puede ser menor a 0.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if edad > 70:
        vacuna='Tipo C'
    elif edad>=16 and edad<=69 and sexo in "Mujer" or sexo in "mujer": 
        vacuna='Tipo B'
    elif edad>=16 and edad<=69 and sexo in "Hombre" or sexo in "hombre": 
        vacuna='Tipo A'    
    else:
        vacuna='Tipo A'

    print(green+f"Como tu edad es {edad} años y eres {sexo}, la vacuna a aplicar el la de {vacuna}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      