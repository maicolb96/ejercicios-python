"""
Determinar la media de una lista de números positivos 
terminada con un número no positivo después del 
último número valido.
"""
import os
os.system("cls")

# Inicializar la lista vacía y la variable para la suma de los números
numeros = []
suma = 0

# Solicitar al usuario ingresar los números hasta que ingrese un número no positivo
while True:
    os.system("cls")
    numero = float(input("Ingrese un número positivo (ingrese un número negativo para terminar): "))
    if numero <= 0:
        break
    numeros.append(numero)
    suma += numero

# Verificar si hay números en la lista antes de calcular la media
if len(numeros) > 0:
    media = suma / len(numeros)
    print("La media de los números ingresados es:", media)
else:
    print("No se ingresaron números positivos.")
