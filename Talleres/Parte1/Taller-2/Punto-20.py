"""
El banco “Bandido de peluche” desea calcular para uno de sus 
clientes el saldo actual, el pago mínimo y el pago para no generar intereses. 
Los datos que se conocen son: saldo anterior del cliente, monto de las compras 
que realizó y el pago que depositó en el corte anterior. Para calcular el pago 
mínimo se debe considerar 15% del saldo actual, y para no generar intereses 
corresponde 85% del saldo actual, considerando que este saldo debe incluir 12% 
de los intereses causados por no realizar el pago mínimo y $200 por 
multa por el mismo motivo.

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
print(green+"Determina el saldo actual, el pago mínimo, el pago para no generar intereses y el pago por intereses para un cliente.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    saldo_anterior = float(input(blue+"Ingrese el saldo anterior del cliente: \n"))
    monto_compras = float(input(blue+"Ingrese el monto de las compras realizadas: \n"))
    pago_anterior = float(input(blue+"Ingrese el pago depositado en el corte anterior: \n"))
        
    saldo_actual = saldo_anterior + monto_compras - pago_anterior
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    pago_minimo = 0.15 * saldo_actual
    saldo_sin_intereses = 0.85 * saldo_actual
    
    if saldo_actual * 0.12 > pago_minimo:
        pago_minimo = saldo_actual * 0.12 + 200
    else:
        pago_minimo = saldo_actual * 0.12
    
    pago_intereses = saldo_actual - saldo_sin_intereses
    
    print(green+f"El saldo actual es: ${saldo_actual}")
    print(green+f"El pago mínimo es: ${pago_minimo}")
    print(green+f"El pago para no generar intereses es: ${saldo_sin_intereses}")
    print(green+f"El pago por intereses es: ${pago_intereses}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      