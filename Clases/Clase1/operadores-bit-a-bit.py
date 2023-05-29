#Se importa la libreria os que permite utilizar codigos de MSDOS
import os
#Operadores Relacionales

"""Ejemplos de operadores bit a bit o (Bitwise) de Python:

   AND:         &     
   OR:          |     
   XOR:         ^     
   NOT:         ~     
   DESPLAZA ->: >>    
   DESPLAZA <-: <<    

   |   AND & (Conjunción) -- (A*B)   |  EJEMPLO: 
   |                                 |
   |             0*0 = 0             |  2 es 010
   |             0*1 = 0             |  5 es 101
   |             1*0 = 0             |  res= 000 -> 0
   |             1*1 = 1             | 

   |   OR | (Disyunción) -- (A+B)    |  EJEMPLO:
   |                                 |
   |             0+0 = 0             |  2 es 010
   |             0+1 = 1             |  5 es 101  
   |             1+0 = 1             |  res= 101 -> 5
   |             1+1 = 1             |
    
   |  XOR ^ (Disyunción exclusiva) -- (A+B)*(!A + !B)  |  EJEMPLO:
   |                                                   |
   |             (0+0)*(1+1) = 0                       |  2 es 010
   |             (0+1)*(1+0) = 1                       |  7 es 111
   |             (1+0)*(0+1) = 1                       |  res= 101 -> 5 
   |             (1+1)*(0+0) = 0                       |

   |   NOT ~ (Negación) (!A)    |  EJEMPLO:
   |                            |  2 es 010 
   |   ~A = -(A(Base 2) + 1)    | ~2 es -(010 + 1)
   |                            | ~2 es -(011)  
   |                            | ~2 es -3
   |                            |
    
"""

"""A continuación se crea un metodo que realiza
   diferentes operaciones de comparación bit por bit 
   y relacion recibiendo por parámetro dos números
"""



def bitWise(num1,num2,opc):

   if opc==1:
      res = num1 & num2
      print("La conjuncion lógica (AND) de ",num1," & ",num2," es: ",res)
   elif opc==2:
      res = num1 | num2
      print("La disyunción lógica (OR) de ",num1," | ",num2," es: ",res)
   elif opc==3:
      res = num1 ^ num2
      print("La disyunción exclusiva lógica (XOR) de ",num1," ^ ",num2," es: ",res)
   elif opc==4:
      res = ~num1
      print("La negación lógica (NOT) de ",num1," es: ",res)
   elif opc==5:
      res = num1 >> 1 
      print("El desplazamiento de 1 bit a la derecha de ",num1," es: ",res)
   elif opc==5:
      res = num1 << 1
      print("El desplazamiento de 1 bit a la izquierda de ",num1," es: ",res)
   else:
      res=1999099123              

def main():

   #Limpia la consola
   os.system('cls')

   #Indica que hace el programa
   print("Este algoritmo opera entre dos numeros comparando sus bites\n")

   #Permite establecer una opcion para operar
   """
   Try es una función que permite ejecutar un codigo
   mientras no halla errores, si hay un error ejecuta 
   lo que hay dentro de la funcion except.
   """
   try:
      opc=int(input(
                 "- 1 para AND &\n" 
                 "- 2 para OR |\n"
                 "- 3 para XOR ^\n"  
                 "- 4 para NOT ~\n"
                 "- 5 para DESPLAZA >>\n"
                 "- 6 para DESPLAZA <<\n"
                 "\n"
                 "Ingrese: "
               ))
      
      #Limpia la consola
      os.system('cls')
   
      #Se capturan los operandos y se asignan a las variables num y num2
      if opc>0 and opc<7:
         num1=int(input("Ingrese el primer numero:\n"))
         num2=int(input("Ingrese el segundo numero:\n"))
      
         #Limpia la consola
         os.system('cls')
      
         #Llama al metodo que compara bit a bit y le manda los parametros
         bitWise(num1,num2,opc) 
      else:
         print("¡Opción no valida!") 
   except Exception as e:
      print("Debes ingresar un número",e)  

main()                     
