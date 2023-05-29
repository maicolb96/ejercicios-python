
from package.Functions import *

"""
Diseñar la función FACTORIAL que calcule 
la factorial de un número entero
entre el rango 100 a 1.000.000.
"""

#Esta función calcula el factorial de unnúmero
def factorial(x):
    sum=x
    for i in range (x,1,-1): sum*= (i-1)  
    return sum

#Esta función se encarga de leer un número verificar si esta entre 100 y 1000000 
def verify_num():
    msj_1="Ingrese un número entre 100 y 1.000.000: \n"
    x=int(input(msj_1))
    res = str(x) if x>=100 and x<=1000000 else msj_1    
    return res

while True:
    try:
        cls()
        res=verify_num()
        #Si el retorno de verify_num no tiene el texto Ingrese, es calculable
        if "Ingrese" not in res: 
            print(f"El factorial de {res} es {factorial(int(res))}")
            break
        else:
            print(res)  
    except ValueError as e:
        print("Error, ingrese un valor válido.")
        sleep(2)

   