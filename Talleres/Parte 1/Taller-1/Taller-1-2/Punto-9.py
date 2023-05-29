"""
Hacer un algoritmo para implementar una calculadora de las 
cuatro operaciones básicas y que le permita al usuario elegir 
que operación va a realizar; con palabras, es decir: 
sumar, restar, multiplicar o dividir.
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("El algoritmo permite realizar las 4 operaciones matemáticas básicas (Sumar-Restar-Multiplicar-Dividir).\n")

#-------------------------------ENTRADAS----------------------------------

#Se pide al usuario que escoja una opción y se asigna a una variable
opc=input("Escoja una operación escribiendo 'Sumar - Restar - Multiplicar - Dividir'\n")

#Se limpia la consola
os.system('cls')

if opc in 'sumar':
    
    suma=0
    string=""

    print("Has escogido sumar\n ")
    
    n=int(input("Cuantos números desea sumar: "))
    print("\n")
    i=0
    #Se ejecuta n veces definidas por el usuario
    for i in range(n):

        #Captura los operandos
        num=float(input("Ingrese el "+str(i+1)+" número: "))

        #Concatena los números ingresados en un string
        if i+1 < n:string=string+str(num)+" + "
        else:string=string+str(num)
        
        #acumula sumando num mas lo anterior
        suma += num
    
    #Se imprime el resultado de la suma.
    print("\nLa suma de ",string," es: ",suma,"\n")

elif opc in 'restar':
    
    resta=0
    string=""

    print("Has escogido restar\n ")
    
    n=int(input("Cuantos números desea restar: "))
    print("\n")
    i=0
    #Se ejecuta n veces definidas por el usuario
    for i in range(n):

        #Captura los operandos
        num=float(input("Ingrese el "+str(i+1)+" número: "))

        #Concatena los números ingresados en un string
        if i+1 < n:string=string+str(num)+" - "
        else:string=string+str(num)
        
        #resta a partir de la segunda iteracion 
        if i == 0:
            resta = num
        else:    
           resta -= num
    
    #Se imprime el resultado de la resta.
    print("\nLa resta de ",string," es: ",resta,"\n")    

elif opc in 'multiplicar' or opc in 'multiplicacion':
    
    multiplicacion=0
    string=""

    print("Has escogido multiplicar\n ")
    
    n=int(input("Cuantos números desea multiplicar: "))
    print("\n")
    i=0
    #Se ejecuta n veces definidas por el usuario
    for i in range(n):

        #Captura los operandos
        num=float(input("Ingrese el "+str(i+1)+" número: "))

        #Concatena los números ingresados en un string
        if i+1 < n:string=string+str(num)+" x "
        else:string=string+str(num)
        
        #multiplica a partir de la segunda iteracion
        if i == 0:
            multiplicacion = num
        else:    
           multiplicacion *= num
    
    #Se imprime el resultado de la suma.
    print("\nLa multiplicación de ",string," es: ",multiplicacion,"\n") 

elif opc in 'dividir' or opc in 'divicion':
    
    divicion=0
    string=""

    print("Has escogido dividir\n ")
    
    n=int(input("Cuantos números desea dividir: "))
    print("\n")
    i=0
    #Se ejecuta n veces definidas por el usuario
    for i in range(n):

        #Captura los operandos
        num=float(input("Ingrese el "+str(i+1)+" número: "))

        #Concatena los números ingresados en un string
        if i+1 < n:string=string+str(num)+" / "
        else:string=string+str(num)
        
        #multiplica a partir de la segunda iteracion
        if i == 0:
            divicion = num
        else:    
           divicion /= num
    
    #Se imprime el resultado de la suma.
    print("\nLa divición de ",string," es: ",divicion,"\n")       