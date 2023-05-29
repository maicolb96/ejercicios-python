"""
sumar los números enteros del 1 al 100 mediante:
Estructura repetir
Estructura mientras
Estructura desde

"""
import os
os.system("cls")
print("Este algoritmo utiliza tres metodos para sumar los números del 1 al 100.")

#Repetir no existe en python pero se emula con un while
i=0;suma=0
while True:
    i+=1; suma+=i
    if i==100: break
print(f"La suma con repetir es: {suma}")

#Suma de los números con mientras
i=0;suma=0
while i<100: i+=1; suma+=i
print(f"La suma con while es: {suma}")

#Suma de los números con mientras
i=0;suma=0
for i in range(100):suma+=(i+1)
print(f"La suma con for es: {suma}")



    

