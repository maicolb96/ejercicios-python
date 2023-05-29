"""
Estos dibujos realizar los algoritmos que lo resuelva

x o o       o o o x o o o
x x o       o o x x x o o
x x x       o x x x x x o
x x o       x x x x x x x
x o o      

o o x       x x x x x x x
o x x       o x x x x x o
x x x       o o x x x o o
o x x       o o o x o o o
o o x
"""
import os
os.system("cls")

def dibujo(l):
    
    matriz = []
    contador_x = 0
    
    for i in range(5):
        fila = []
        for j in range(3):
            if j <= contador_x:fila.append('x')
            else:fila.append('o')
        matriz.append(fila)

        if i<=2:contador_x += 1
        else:contador_x -= 1    
        if contador_x >= 3:contador_x = 1

    for i in range(l[1],l[2],l[3]):
        for j in range(l[4],l[5],l[6]):
            if l[0]<=2:print(matriz[i][j], end=' ')
            if l[0]>2:print(matriz[j][i], end=' ')
        print()
    print()

mat=[[1,0,5,1,0,3,1],[2,4,-1,-1,2,-1,-1],[3,0,3,1,4,-1,-1],[4,2,-1,-1,4,-1,-1]]
for row in mat:dibujo(row) 

       

