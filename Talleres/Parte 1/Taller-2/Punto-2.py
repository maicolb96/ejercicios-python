""" 
El 14 de febrero una persona desea comprarle un regalo al 
ser querido que más aprecia en ese momento, su dilema radica 
en qué regalo puede hacerle, las alternativas que 
tiene son las siguientes: 

Regalo    |  Costo            |
-------------------------------
Tarjeta   |  $10.00 o menos   | 
Chocolates|  $11.00 a $100.00 |
Flores    |  $101.00 a $250.00| 
Anillo    |  Más de $251.00   |

"""

#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color

#Utiliza la función system para limpiar la consola
os.system('cls')

#Inicializa la variable start en verdader
start=True
print("Este algoritmo determina el regalo que puedes comprar segun el dinero que tienes.\n")

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#El ciclo se ejecuta mientras start sea verdadero
while start:
    
    """
    Try
    Verifica si hay errores en la ejecución, en try se ejecuta
    el código sin errores.
    Except
    En except se ejecuta el código cuando hay un error.
    """
    try:
        cash=float(input(blue+"Ingrese la cantidad de dinero que tienes: \n"))
       
        #Se verifica si los datos ingresados son negativos
        if cash<0:
            os.system('cls')
            print(red+"El monto no puede ser menor a $0.\n")
        else:
            #Si los datos son positivos cambia el estado de start y sale del ciclo
            start=False 
    except:
        os.system('cls')
        print(red+"Ha ocurrido un error, vuelva a ingresar los datos.\n")
      

#Define que puede comprar según el valor de la variable cash y lo imprime
if cash==0:
    print(red+f"\nLo siento, no tienes dinero para regalar algo.\n")
elif cash<=10:
    print(green+f"\nComo solo tienes ${cash} puedes regalar una Tarjeta.\n")
elif cash>10 and cash<=100:
    print(green+f"\nComo solo tienes ${cash} puedes regalar Chocolates.\n")    
elif cash>100 and cash<=250:
    print(green+f"\nComo solo tienes ${cash} puedes regalar Flores.\n") 
elif cash>250:
    print(green+f"\nComo solo tienes ${cash} puedes regalar un Anillo.\n")             
        
   