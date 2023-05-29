""" 
Se tiene el nombre y la edad de tres personas. 
Se desea saber el nombre y la edad de la persona 
de menor edad. Realice el algoritmo correspondiente.
"""


#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color
#Importando la libreria numpy
import numpy as np

#Utiliza la función system para limpiar la consola
os.system('cls')

#Inicializa la variable start en verdader
start=True
print("Este algoritmo muestra el nómbre y la edad de el menor de 3 personas.\n")

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#El ciclo se ejecuta mientras start sea verdadero
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    opc=int(input(blue+"Ingrese 1 pra usar el metodo 1: \n"+ 
                  blue+"Ingrese 2 para usar el metodo 2: \n"
    ))
    os.system('cls')
    
    match opc:
        case 1:
            nombre_1=input(blue+"Ingrese el nombre 1: \n")
            edad_1=int(input(blue+"Ingrese la edad 1: \n"))

            nombre_2=input(blue+"Ingrese el nombre 2: \n")
            edad_2=int(input(blue+"Ingrese la edad 2: \n"))
            
            nombre_3=input(blue+"Ingrese el nombre 3: \n")
            edad_3=int(input(blue+"Ingrese la edad 3: \n"))                        
                
            if edad_2<edad_1 and edad_2<edad_3:
                menor_edad=edad_2
                menor_nombre=nombre_2
            elif edad_1<edad_2 and edad_1<edad_3:
                menor_edad=edad_1
                menor_nombre=nombre_1
            elif edad_3<edad_2 and edad_3<edad_1:
                menor_edad=edad_3   
                menor_nombre=nombre_3
                       
        case 2:   
            i=0
            edad=[0,0,0]
            nombre=['a','b','c']
             
            while i<3:
                nombre[i]=input(blue+f"Ingrese el nombre {i+1}: \n")
                edad[i]=int(input(blue+f"Ingrese la edad {i+1}: \n"))
                os.system('cls')
                i+=1  
            
            menor_edad=np.amin(edad)
            index=np.where(edad==np.amin(edad))
            menor_nombre=nombre[index[0][0]]
                
    print(f"El menor es {menor_nombre} con {menor_edad} años.")                       
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      