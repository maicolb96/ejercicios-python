from package.Functions import *

"""
19.escribir un algoritmo que convierta los números 
arábigos en números romanos y viceversa 
I=1, V=5, X=10, L=50,C=100, D=500 y M=1000.
"""

def arabigo_a_romano(num):
 
    valores = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
    romano = ""
    
    for valor, letra in valores:
        while num >= valor:
            romano += letra
            num -= valor
    return romano

def romano_a_arabigo(romano):

    # Diccionario de valores romanos y sus equivalentes arábigos
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

    arabigo = 0
    for i in range(len(romano) - 1, -1, -1):
        valor = valores[romano[i]]
        # Si el valor arábigo del carácter actual es menor que el siguiente,
        # restar su valor al número arábigo. De lo contrario, sumarlo.
        if i < len(romano) - 1 and valores[romano[i+1]] > valor: arabigo -= valor
        else: arabigo += valor
    return arabigo


cls()
try:
    opc=input("Ingrese 1 para romano a arabigo\nIngrese 2 para arabigo a romano\n")
    num=input("Ingrese el número: ")
    if opc=="1":print(f"El número {num} es el {romano_a_arabigo(num.upper())} arabigo.")
    elif opc=="2":print(f"El número {num} es el {arabigo_a_romano(int(num))} romano.")
    else:print("Opción no valida.")
except:
    print("Error, verifique los datos ingresados.")    