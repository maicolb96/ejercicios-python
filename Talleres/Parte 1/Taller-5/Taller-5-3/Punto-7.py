"""
Imprimir de la siguiente matriz la diagonal segundaria:

25 12 26 7 15
12 12 2 9 25
25 6 4 25 6
"""
import os,random
os.system("cls")


matriz = [[25, 12, 26, 7, 15],
          [12, 12, 2, 9, 25],
          [25, 6, 4, 25, 6]]

print("La matriz original es: \n")
for row in matriz:print(row)

print("\nLa diagonal secundaria es:")
for i in range(3):
    for j in range(4,1,-1):
        if i==0 and j==4:print(matriz[i][j],end=" ")
        if i==1 and j==3:print(matriz[i][j],end=" ")
        if i==2 and j==2:print(matriz[i][j],end=" ")
       


