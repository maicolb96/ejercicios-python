"""
Un almacén que vende zapatos a un precio fijo desea conocer 
a cuanto asciende su utilidad en el total de las ventas, 
partiendo del número de artículos vendidos por día. 
Se conoce que la utilidad es del 35%
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("Este algoritmo calcula la utilidad total de las ventas de zapatos partiendo de la cantidad\n")

#-------------------------------ENTRADAS----------------------------------
#Captura el precio y cantidad de items vendidos
PRICE = float(input("Ingrese el precio de los zapatos:\n"))
items_sold=int(input("Ingrese la cantidad de articulos que vendió:\n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula la utilidad por item y total
utility_by_item=0.35*PRICE
total_utiliy=items_sold*utility_by_item

#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("La utilidad total es: $",total_utiliy)

