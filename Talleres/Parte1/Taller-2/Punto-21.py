"""
Un profesor tiene un salario inicial de $1500, y recibe un incremento
 de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? 
 ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo.
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
print(green+"Determina el incremento en el salario anual de un profesor.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    print("Historial de salario de los ultimos 6 años:\n")
    sueldo=1500

    for i in range(6):
        if i>0:
            sueldo=sueldo+(sueldo*0.10)
        print(f"Año {i+1}: ${sueldo}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      