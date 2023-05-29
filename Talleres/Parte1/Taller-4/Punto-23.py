"""
Un vendedor recibe un sueldo base más un 10% extra por comisión
de sus ventas, el vendedor desea saber cuánto dinero obtendrá 
por concepto de comisiones por las tres ventas que realiza en 
el mes y el total que recibirá en el mes tomando en cuenta su 
sueldo base y comisiones.
"""

import os
os.system("cls")

ventas=[]
comision=0

print("Este algoritmo calcula el sueldo mas comisión de un vendedor.")

sueldo=float(input("Ingrese el suelado base: \n"))
for i in range(3):
    ventas.append(float(input(f"Ingrese el valor de la venta {i+1}: \n")))

c=0
os.system("cls")
print(f"Sueldo base: ${sueldo}")
for item in ventas:
   c+=1
   comision+=item*0.10
   print(f"Comisión de la venta {c}: ${item*0.10:.2f}")
print(f"Total comisiones: ${comision:.2f}")   
print(f"Total a pagar: ${comision+sueldo:.2f}")