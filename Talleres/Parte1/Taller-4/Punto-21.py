#Importa la libreria os, consular documentación de python
from datetime import date
import os

"""
Realizar un algoritmo que calcule la edad de una persona.
"""
print("Este algoritmo calcula la edad de una persona.")

#Se limpia la consola
os.system('cls')

#Captura la fecha de nacimiento y se asigna a una variable
print("Ingrese la fecha de nacimiento\n ")
dia=int(input("DIA: ")); mes=int(input("MES: ")); año=int(input("AÑO: "))

#-------------------------------PROCESOS----------------------------------
#Se resta la fecha actual con la de nacimiento y devuelve los años, meses y dias.
dia2=(date.today().day)-dia
mes2=(12+(date.today().month))-mes
año2=(date.today().year)-año  

#Se verifica si el mes de nacimiento esta por encima o por debajo del mes actual
if mes>int(date.today().month):año2=año2-1
else:mes2=mes2-12 
        
#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print(f"\nTienes {año2} años.")

