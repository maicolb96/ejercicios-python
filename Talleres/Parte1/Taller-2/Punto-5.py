"""
El presidente de la república ha decidido estimular 
a todos los estudiantes de una universidad mediante 
la asignación de becas mensuales, para esto se tomarán 
en consideración los siguientes criterios: 

Para alumnos mayores de 18 años con promedio mayor 
o igual a 9, la beca será de $2000.00; con promedio mayor 
o igual a 7.5, de $1000.00; para los promedios menores de 7.5 
pero mayores o iguales a 6.0, de $500.00; a los demás se les 
enviará una carta de invitación invitándolos a que estudien más 
en el próximo ciclo escolar. A los alumnos de 18 años o menores 
de esta edad, con promedios mayores o iguales a 9, se les dará $3000; 
con promedios menores a 9 pero mayores o iguales a 8, $2000; 
para los alumnos con promedios menores a 8 pero mayores o iguales a 6, 
se les dará $100, y a los alumnos que tengan promedios menores a 6 se 
les enviará carta de invitación.
"""
#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color
#Importando la libreria numpy
import numpy as np

#Utiliza la función system para limpiar la consola
os.system('cls')

#Inicializa la variable start en verdader
start=True
print("EMuestra las becas que se deben asignar a los estudiantes según algunos criterios.\n")

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se asignan los valores de edad y promedio a las variables correspondientes
    nombre=input(blue+"Ingrese el nombre del estudiante:\n")
    edad=int(input(blue+"Ingrese la edad del estudiante:\n"))
    promedio=float(input(blue+"Ingrese el promedio alcanzado:\n"))
    
    #Se compara la variable edad y promedio y se realiza una acción segun cada caso.
    if edad>18 and promedio < 7.5 and promedio >= 6.0:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $500.00"))
    elif edad>18 and promedio >= 7.5 and promedio < 9:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $1000.00"))
    elif edad>18 and promedio >= 9: 
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $2000.00"))
    elif edad<=18 and promedio < 6.0:
        print(red+(f"Lo siento {nombre}, no has ganado la beca, te invitamos a mejorar."))
    elif edad<=18 and promedio < 8 and promedio >= 6.0:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $100.00"))
    elif edad<=18 and promedio >= 8 and promedio < 9:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $2000.00"))
    elif edad<=18 and promedio >= 9: 
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de una beca por $3000.00"))
                          
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      