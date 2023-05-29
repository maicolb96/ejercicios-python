"""
“El náufrago satisfecho” ofrece hamburguesas sencillas 
(S), dobles (D) y triples (T), las cuales tienen un costo 
de $20, $25 y $28 respectivamente. La empresa acepta tarjetas 
de crédito con un cargo de 5 % sobre la compra. Suponiendo que los 
clientes adquieren N hamburguesas, las cuales pueden ser de diferente 
tipo, realice un algoritmo para determinar cuánto deben pagar.
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
print(green+"Determina el valor a pagar por una hamburguesa.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    tipo_hamburguesa = input(blue+"Ingrese el tipo de hamburguesa (Sencilla - Doble - Triple): \n")
    cantidad = int(input(blue+"Ingrese la cantidad de hamburguesas a comprar: \n"))
    medio_pago = input(blue+"Ingrese el metodo de pago (Tarjeta - Efectivo): \n")
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if tipo_hamburguesa in "Sencilla" or tipo_hamburguesa in "sencilla":
        costo=20
    elif tipo_hamburguesa in "Doble" or tipo_hamburguesa in "doble":
        costo=25 
    elif tipo_hamburguesa in "Triple" or tipo_hamburguesa in "triple":
        costo=28
    else:
        costo=0

    if medio_pago in "Tarjeta" or medio_pago in "tarjeta" :
        cargo=(0.05*costo)*cantidad
    else:
        cargo=0 

    
    costo_total=(costo*cantidad)+cargo

    print(green+f"Has comprado {cantidad} Hamburgesas {tipo_hamburguesa}s.")
    print(green+f"El metodo de pago es {medio_pago}, cobros adicionales ${cargo} y el total a pagar es de ${costo_total}")
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      

      