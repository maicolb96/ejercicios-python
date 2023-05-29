#Operadores Aritmeticos

"""Ejemplos de operadores aritmeticos de Python:
   Suma: +
   Resta: -
   Multiplicacion: *
   Division: /
   Modulo: % 
   Potencia: **
"""

"""A continuación se crean metodos que realizan
   diferentes operaciones algebraicas recibiendo por
   parámetro dos números
"""

#Se importa la librería OS que permite manejar comandos por consola
import os


def sumar(num1,num2):
   res=num1+num2
   print("La suma de ",num1," mas ",num2," es igual a ",res)

def restar(num1,num2):
   res=num1-num2
   print("La resta de ",num1," menos ",num2," es igual a ",res)

def multiplicar(num1,num2):
   res=num1*num2
   print("La multiplicacion de ",num1," multiplicado ",num2," es igual a ",res)

def dividir(num1,num2):
   res=num1/num2
   print("La división de ",num1," dividido ",num2," es igual a ",res)

def modular(num1,num2):
   res=num1%num2
   print("El modulo de ",num1," mod ",num2," es igual a ",res)

def potenciar(num1,num2):
   res=num1**num2
   print("La potencia de ",num1," elevado a ",num2," es igual a ",res)

def dividirExacto(num1,num2):
   res=num1//num2
   print("La division exacta de ",num1," dividido ",num2," es igual a ",res)

#Metodo principal
def main():

   #Limpia la consola
   os.system('cls')

   #Indica que hace el programa
   print("Este programa realiza operaciones aritmeticas básicas\n")

   #Permite establecer una opcion para operar

   """
   Try es una función que permite ejecutar un codigo
   mientras no halla errores, si hay un error ejecuta 
   lo que hay dentro de la funcion except.
   """
   try:
      opc=int(input(
                 "- 1 para sumar\n"
                 "- 2 para restar\n"
                 "- 3 para multiplicar\n"
                 "- 4 para dividir\n"
                 "- 5 para modular\n"
                 "- 6 para potenciar\n"
                 "- 7 para dividir exacto\n"
                 "\n"
                 "Ingrese: "
               ))
      
      #Limpia la consola
      os.system('cls')
   
      #Se capturan los operandos y se asignan a las variables num y num2
      if opc>0 and opc<8:
         num1=input("Ingrese el primer numero:\n")
         num2=input("Ingrese el segundo numero:\n")
      
         #Limpia la consola
         os.system('cls')
      
         #Verifica la opcion ingresada y realiza una acción segun dicha opcion
         if opc==1:
            #Se llama al método y se pasan 2 parametros numericos
            sumar(int(num1),int(num2))
         elif opc==2:
            #Se llama al método y se pasan 2 parametros numericos
            restar(int(num1),int(num2))
         elif opc==3:
            #Se llama al método y se pasan 2 parametros numericos
            multiplicar(int(num1),int(num2))
         elif opc==4:
            #Se llama al método y se pasan 2 parametros numericos
            dividir(int(num1),int(num2))
         elif opc==5:
            #Se llama al método y se pasan 2 parametros numericos
            modular(int(num1),int(num2))
         elif opc==6:
            #Se llama al método y se pasan 2 parametros numericos
            potenciar(int(num1),int(num2))
         elif opc==7:
            #Se llama al método y se pasan 2 parametros numericos
            dividirExacto(int(num1),int(num2))   
      else:
         print("¡Opción no valida!") 
   except:
      print("Debes ingresar un número")  

main()                     
