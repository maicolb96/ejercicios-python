"""
Se desea saber el total de una caja registradora de un almacén,
se conoce el número de billetes y monedas, así como su valor.
Realice un algoritmo para determinar el total.
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
print(green+"Este algoritmo determina cuál es la edad promedio de cada uno de los M salones y cuál es la edad promedio de toda la escuela.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    # Pedimos al usuario que ingrese el número de billetes y monedas y su valor respectivo
    num_billetes_1000 = int(input("Ingrese el número de billetes de $1000: "))
    num_billetes_2000 = int(input("Ingrese el número de billetes de $2000: "))
    num_billetes_5000 = int(input("Ingrese el número de billetes de $5000: "))
    num_billetes_10000 = int(input("Ingrese el número de billetes de $10000: "))
    num_billetes_20000 = int(input("Ingrese el número de billetes de $20000: "))
    num_billetes_50000 = int(input("Ingrese el número de billetes de $50000: "))
    num_billetes_100000 = int(input("Ingrese el número de billetes de $100000: "))
    num_monedas_50 = int(input("Ingrese el número de monedas de $50: "))
    num_monedas_100 = int(input("Ingrese el número de monedas de $100: "))
    num_monedas_200 = int(input("Ingrese el número de monedas de $200: "))
    num_monedas_500 = int(input("Ingrese el número de monedas de $500: "))
    num_monedas_1000 = int(input("Ingrese el número de monedas de $1000: "))
    
    # Calculamos el total
    total = (num_billetes_1000 * 1000) + (num_billetes_2000 * 2000) + (num_billetes_5000 * 5000) + (num_billetes_10000 * 10000) + (num_billetes_20000 * 20000) + (num_billetes_50000 * 50000) + (num_billetes_100000 * 100000) + (num_monedas_50 * 50) + (num_monedas_100 * 100) + (num_monedas_200 * 200) + (num_monedas_500 * 500) + (num_monedas_1000 * 1000)
    
    # Imprimimos el resultado
    print("El total de la caja registradora es:", total)  

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      

      

      