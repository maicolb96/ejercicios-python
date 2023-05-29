"""
Diseñar un algoritmo para que lea una fecha de nacimiento 
de una persona, luego imprima lo siguiente: Numero de años 
– meses- días, tener en cuenta las fechas antes y después del
cumpleaños.
"""
#Importa la libreria os, consular documentación de python
from datetime import date
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("El algoritmo imprime el número de años, meses y dias que tiene según la fecha de nacimiento.\n")

#-------------------------------ENTRADAS----------------------------------

opc=int(input("Ingrese 1 para calcular con el metodo 1\n"
        "Ingrese 2 para calcular con el metodo 2\n"))

#Se limpia la consola
os.system('cls')

print("Has ingresado la opción ",opc,"\n ")

match opc:
    
    case 1:

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
        
    case 2:
        
        #Captura la fecha de nacimiento y se asigna a una variable
        print("Ingrese la fecha de nacimiento\n ")
        dia=int(input("DIA: ")); mes=int(input("MES: ")); año=int(input("AÑO: "))
    
        print("\nIngrese la fecha actual\n ")
        dia2=int(input("DIA: ")); mes2=int(input("MES: ")); año2=int(input("AÑO: "))  
    
        total_dias= (año*365) + (mes*30) + dia
    
        total_dias2= (año2*365) + (mes2*30) + dia2
    
        res= total_dias2-total_dias
    
        if dia2-dia >= 0:
            dia2 = dia2-dia
        elif dia2-dia < 0 and mes2==2:
            dia2 = 29-dia+dia2
        elif dia2-dia < 0 and (mes2==1 or mes2==3 or mes2==5 or mes2==7 or mes2==8 or mes2==10 or mes2==12):
            dia2 = 31-dia+dia2 
        else:
            dia2 = 30-dia+dia2        
    
        año2 = int(res/365)
        mes2 = int((res%365)/30) 

#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("\nTiempo transcurrido desde ",dia,"-",mes,"-",año,
      " hasta ",date.today().day,"-",date.today().month,
      "-",date.today().year,"\n",año2," años, ",mes2," meses y ",dia2," dias.\n")

