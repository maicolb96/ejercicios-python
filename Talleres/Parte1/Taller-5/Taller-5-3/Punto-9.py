"""
Hacer un tablero de ajedrez
"""
import os,random
os.system("cls")

matriz=[[0 for _ in range(7)]for _ in range(7)]

for i in range(7):
    for j in range(7):
        if (i+j)%2==0:matriz[i][j]="  "
        else:matriz[i][j]="██"        

for row in matriz:
    for item in row:
        print(item,end="")
    print()   
    
     