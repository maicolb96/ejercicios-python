""" 
Realice un algoritmo para determinar el sueldo 
semanal de un trabajador con base en las horas 
trabajadas y el pago por hora, considerando que 
después de las 40 horas cada hora se considera 
como excedente y se paga el doble.
"""
#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color

#Utiliza la función system para limpiar la consola
os.system('cls')

#Inicializa la variable start en verdader
start=True
print("Este algoritmo calcula el salario según horas trabajadas y valor po hora.\n")

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#El ciclo se ejecuta mientras start sea verdadero
while start:

    try:
        horas_trabajadas=float(input(blue+"Ingrese las horas trabajadas: \n"))
        valor_hora=float(input(blue+"Ingrese el valor de la hora: \n"))
        
        #Se verifica si los datos ingresados son negativos
        if horas_trabajadas<0 or valor_hora <0:
            os.system('cls')
            print(red+"Las horas trabajadas o el valor por hora no " 
                  "pueden ser menores a cero.\n")
        else:
            #Si los datos son positivos cambia el estado de start y sale del ciclo
            start=False 
    except:
        os.system('cls')
        print(red+"Ha ocurrido un error, vuelva a ingresar los datos.\n")
      

#Si las horas trabajadas no exceden las 40h se realiza una multiplicación básica
if horas_trabajadas<41:
    
    #NOTA: la f indica que es un f-string que permite incrustar expreciones
    print(green+(f"El pago correspondiente por {horas_trabajadas} "
          f"horas trabjadas es ${horas_trabajadas*valor_hora}\n"
    ))
#Si las horas trabajadas exceden las 40, la multiplicación es compuesta    
elif horas_trabajadas>40:
    
    #NOTA: la f indica que es un f-string que permite incrustar expreciones
    print(green+(f"El pago correspondiente por {horas_trabajadas} "
          f"horas trabjadas es ${horas_trabajadas*(valor_hora*2)}\n"
    ))    
   