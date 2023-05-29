"""
Calcular el interés que gana un capital de x pesos
a una tasa de interés del 15% anual en un periodo de n años.
"""
import os
os.system("cls")

sum_intereses=0

print("Este algoritmo calcula el interés que gana un capital de x pesos a una tasa de interés del 15% anual en un periodo de n años.\n")
capital=float(input("Ingrese el capital a invertir: "))
años=int(input("Ingrese la cantidad de años: "))

os.system("cls")
print(f"\nEl capital invertido es de: ${capital}")
for i in range(años):
    sum_intereses+=(capital*0.15)
    print(f"Los intereses del año {i+1} son: ${capital*0.15}")
print(f"Los intereses totales en {años} años son de: ${sum_intereses}")
print(f"El retorno total en {años} años es de: ${sum_intereses+capital}")