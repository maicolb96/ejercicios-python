"""
Una tienda ofrece un descuento del 15% sobre el total 
de la compra y un cliente desea saber cuánto deberá pagar 
finalmente por su compra.
"""
import os
os.system("cls")

print("Este algoritmo indica cuanto debe pagar un cliente con descuento del 15%.\n")

costo=float(input("Ingrese el costo total a pagar: \n"))

print(f"Costo total de articulos: ${costo}\n"
      f"Descuento de 15%: ${costo*0.15}\n"
      f"Total a pagar: ${costo-(costo*0.15)}\n")