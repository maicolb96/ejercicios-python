"""
Realizar un vector que tenga almacenada las vocales, 
otro vector donde tenga almacenado el abecedario, 
cuando esté listo, el usuario pueda ver la posición 
de dichas letras, el objetivo es que pueda digitar 
los números de la posiciones y armar palabras de 
3, 5 o 6 letras.
"""

import os
os.system("cls")

abc=["a","b","c","d","e","f","g","h","i",
     "j","k","l","m","n","ñ","o","p","q",
     "r","s","t","u","v","w","x","y","z"]

index=[]

i=3;j=0

for _ in range(7):
    print([f"Letra: {item} Indice: {abc.index(item)}" for item in abc 
           if abc.index(item)<=i and abc.index(item)>=j], end=" " )
    print();i+=4;j+=4
print("\nSi desea terminar de ingresar letras escriba salir.\n")

i=0
while True:
    i+=1
    opc=input(f"Ingrese un indice para escoger la letra #{i}: ")
    if opc!="salir":index.append(int(opc)) 
    else: break 

for item in index:print(abc[item],end="" )
