#Imprimir todos los números no primos entre 2 y 1000 inclusive.

import os
os.system("cls")

print("Este algoritmo imprime todos los números no primos entre 2 y 1000 inclusive.\n")

count=0
k=0

for i in range(2,1001,1):
    for j in range(i,0,-1):
        if i%j==0:count+=1
    if count<=2:print(i, end=" ")
    count=0            
