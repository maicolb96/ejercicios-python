"""
Una distribuidora de huevos quiere contratarlo a usted 
para que realice un algoritmo que calcule el precio de 
venta para una cantidad de huevos a llevar por un 
determinado cliente. Guiándose por la siguiente información:



Precio unitario Huevo  |  Descuento por cantidades a llevar
 Tipo A  |  Tipo AA    |  1-100 | 101-200 | 201-300 | >= a 301
   220   |    250      |    3%  |    5%   |    8%   |   10%


"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("El algoritmo calcula el valor a pagar por la cantidad de huevos comprados segun su tipo.\n")

#-------------------------------ENTRADAS----------------------------------

huevoA=int(input("Ingrese la cantidad de huevos tipo A: \n"))
huevoAA=int(input("Ingrese la cantidad de huevos tipo AA: \n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula el costo total sin descuento
total=(huevoA*220)+(huevoAA*250)

#Se verifica el descuento a aplicar
if huevoA+huevoAA <= 100: desc=0.03
elif huevoA+huevoAA >= 101 and huevoA+huevoAA <= 200: desc=0.05
elif huevoA+huevoAA >= 201 and huevoA+huevoAA <= 300: desc=0.08
elif huevoA+huevoAA >= 301: desc=0.1
else: desc=0;total = 0 

total -= total*desc
#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("El total a pagar por ",huevoA," huevos tipo A y ",huevoAA," huevos tipo AA es de $",total," \nSe le aplico un descuento del ",desc*100,"%.\n")

