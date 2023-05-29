"""
Una compañía de seguros para autos ofrece dos tipos de póliza: 
cobertura amplia (A) y daños a terceros (B). Para el plan A, 
la cuota base es de $1,200, y para el B, de $950. A ambos planes 
se les carga 10% del costo si la persona que conduce tiene por 
hábito beber alcohol, 5% si utiliza lentes, 5% si padece alguna 
enfermedad –como deficiencia cardiaca o diabetes–, y si tiene más 
de 40 años, se le carga 20%, de lo contrario sólo 10%. Todos estos 
cargos se realizan sobre el costo base. Realice diagrama de flujo y 
diagrama N/S que represente el algoritmo para determinar cuánto le 
cuesta a una persona contratar una póliza.

"""
#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color
#Importando la libreria numpy
import numpy as np

#Utiliza la función system para limpiar la consola
os.system('cls')

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#Inicializa la variable start en verdader
start=True
print(green+"Muestra el costo de una polisa A y una polisa B según algunas condiciones.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    state=True
    total=0.0
    cargo_alcohol=0.0
    cargo_lentes=0.0
    cargo_enfermedad=0.0
    
    #Se asignan los valores capturados por consola a las variables correspondientes
    nombre=input(blue+"Ingrese el nombre:\n")
    edad=int(input(blue+"Ingrese la edad:\n"))
    
    #Se define el costo del plan segun el tipo
    while state==True:
        
        plan=input(blue+"Ingrese el tipo de plan A o B:\n")
        if plan == "A" or plan == "a":costo=1200;state=False
        elif plan == "B" or plan == "b":costo=950;state=False
        elif plan != "A" or plan != "B" or plan != "a" or plan != "b":
            os.system('cls')
            print("El plan ingresado es incorrecto, vuelva ingresar un plan A o B")
           
        
    alcohol=input(blue+"Bebe alcohol con frecuencia, responda si o no:\n")
    lentes=input(blue+"Usa lentes, responda si o no:\n")
    enfermedad=input(blue+"Padece deficiencia cardiaca o diabetes, responda si o no:\n")
          
    os.system('cls')      
    #Se compara las variable y se realiza una acción segun cada caso.
    if alcohol=='si':
        cargo_alcohol=(costo*0.10)
        print("Cargo por consumo de alcohol: $",cargo_alcohol)
    if lentes=='si':
        cargo_lentes=(costo*0.05)
        print("Cargo por uso de lentes: $",cargo_lentes)
    if enfermedad=='si' and edad > 40:
        cargo_enfermedad=(costo*0.20)
        print("Cargo por enfermedad: $",cargo_enfermedad)
    elif enfermedad=='si' and edad <= 40:
        cargo_enfermedad=(costo*0.10) 
        print("Cargo por enfermedad: $",cargo_enfermedad)
    
    print(f"Costo bruto del plan {plan}: ${costo}\n")    
    print(green+f"Hola {nombre}, el valor a pagar por el plan {plan} es de ${costo+cargo_alcohol+cargo_enfermedad+cargo_lentes}")             
   
                          
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      