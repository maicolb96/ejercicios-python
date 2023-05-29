"""
Leer por pantalla un número entre 1 y 12, luego imprimir 
en letras el mes a que corresponde dicho valor y a que signo 
del zodiaco pertenece, ejemplo: si es mes de Mayo, los
signos a que corresponde son: Tauro-Geminis.
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("El algoritmo pide un número e imprime su mes equivalente y signos zodiacales.\n")

#-------------------------------ENTRADAS----------------------------------
#Captura el número del mes y se asigna a una variable
num=int(input("Ingrese el número del mes:\n"))

#-------------------------------PROCESOS----------------------------------
#Se comparan los números verificando cual es el menor, el mayor y el medio

if num==1:
    mes="Enero"
    singos="Acuario - Capricornio"
elif num==2:
    mes="Febrero"
    singos="Acuario - Piscis"  
elif num==3:
    mes="Marzo"
    singos="Aries - Piscis"   
elif num==4:
    mes="Abril"
    singos="Aries - Tauro"  
elif num==5:
    mes="Mayo"
    singos="Géminis - Tauro" 
elif num==6:
    mes="Junio"
    singos="Géminis - Cancer"  
elif num==7:
    mes="Julio"
    singos="Cancer - Leo"         
elif num==8:
    mes="Agosto"
    singos="Leo - Virgo"  
elif num==9:
    mes="Septiembre"
    singos="Virgo - Libra"  
elif num==10:
    mes="Octubre"
    singos="Libra - Escorpio"   
elif num==11:
    mes="Noviembre"
    singos="Escorpio - Sagitario"   
elif num==12:
    mes="Diciembre"
    singos="Sagitario - Capricornio"                              
#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("El número ingresado ",num," corresponde al mes ",mes," y sus signos zodiacales son ",singos)
