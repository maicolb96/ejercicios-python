#Se importa la libreria os que permite utilizar codigos de MSDOS
import os
#Operadores Relacionales

"""Ejemplos de operadores relacionales de Python:
   Mayor Que:     >
   Menor Que:     <
   Igualdad:      ==   
   Mayor o Igual: >=
   Menor o Igual: <=
   Diferencia:    != 
"""

"""A continuación se crea un metodo que realiza
   diferentes operaciones de comparación y relacion 
   recibiendo por parámetro dos números
"""

def compareNumbers(num1,num2):

    if num1>num2:
        print("El número ",num1," es mayor que el número ",num2)
    if num1<num2:
        print("El número ",num1," es menor que el número ",num2) 
    if num1==num2:
        print("El número ",num1," es igual a el número ",num2)
    if num1>=num2:
        print("El número ",num1," es mayor o igual que el número ",num2)
    if num1<=num2:
        print("El número ",num1," es menor o igual que el número ",num2)
    if num1!=num2:
        print("El número ",num1," es diferente que el número ",num2)    


#Metodo principal
def main():

    #Limpia la consola
    os.system('cls')

    print("Este programa compara dos números y muestra si son mayores, menores, iguales o diferente")                       

    #Se leen dos valores por consola y son asignados a dos variables
    num1=int(input("Ingrese el número 1:\n"))
    num2=int(input("Ingrese el número 2:\n"))

    #Limpia la consola
    os.system('cls')

    #Se llama al método que conpara los números y se pasan los dos numeros como parametros
    compareNumbers(num1,num2)

#Se llama al metodo principal
main()    
