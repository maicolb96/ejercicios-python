"""
Leer tres valores por pantalla, determinar e 
imprimir el mayor, el medio y el menor.
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("Este algoritmo imprimir el mayor, el medio y el menor de una lista de números.\n")

#-------------------------------ENTRADAS----------------------------------
#Captura tres números y se guarda cada uno en una variable
num1=float(input("Ingrese el primer número:\n"))
num2=float(input("Ingrese el segundo número:\n"))
num3=float(input("Ingrese el tercer número:\n"))

#-------------------------------PROCESOS----------------------------------
#Se comparan los números verificando cual es el menor, el mayor y el medio

if num1 < num2 and num1 < num3:
    menor=num1
    
    if num2>num3:
        mayor=num2
        medio=num3
    else:
        mayor=num3 
        medio=num2 

elif num2 < num1 and num2 < num3: 
    menor=num2
    
    if num1>num3:
        mayor=num1
        medio=num3
    else:
        mayor=num3 
        medio=num1 
        
elif num3 < num1 and num3 < num2: 
    menor=num3
    
    if num2>num1:
        mayor=num2
        medio=num1
    else:
        mayor=num1 
        medio=num2                
#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("Los números ingresados son: ",num1," - ",num2," - ",num3,"\n")
print("El mayor es el ",mayor,"\nEl del medio es el ",medio,"\nEl menor es el ",menor)
