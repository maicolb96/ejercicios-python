"""
Este programa recorre simultáneamente los vectores del 
punto 1, 2, 3 y muestra la posición y el resultado.
"""

import os
os.system("cls")

print("Este programa recorre simultáneamente los vectores del\n" 
      "punto 1, 2, 3 y muestra la posición y el resultado.\n" )

v1 =[i for i in range(1,40,2)]
v2=[i for i in range(2,31,2)]
v3=[1,2,6];v3+=([i for i in range(9,33,3)])
v4=[v1,v2,v3]

dic={1:"Vector del punto 1:", 2:"Vector del punto 2:", 3:"Vector del punto 3:"}
def printer(v):
    for i in v:print(f"Indice[{v.index(i)}] = {i}")
i=0
for item in v4: i+=1; print(dic.get(i,None)); printer(item); print("\n")



