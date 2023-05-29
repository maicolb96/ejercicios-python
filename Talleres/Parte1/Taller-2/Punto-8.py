"""
Represente un algoritmo mediante un diagrama de flujo
y el pseudocódigo para determinar a qué lugar podrá ir 
de vacaciones una persona, considerando que la línea de 
autobuses “La tortuga” cobra por kilómetro recorrido. 
Se debe considerar el costo del pasaje tanto de ida, 
como de vuelta; los datos que se conocen y que son fijos son: 
México, 750 km; P.V., 800 km; Acapulco, 1200 km, y Cancún, 1800 km. 
También se debe considerar la posibilidad de tener que quedarse en casa.
"""
#Importando libreria os que permite interactuar con el SO
import os
#Importando libreria colour que permite cambiar colores
from colored import fg as color

#Utiliza la función system para limpiar la consola
os.system('cls')

#Definiendo colores para el texto
blue=color('blue')
red=color('red')
green=color('green')

#Inicializa la variable start en verdader
start=True
print(green+"Muestra a qué lugar podrá ir de vacaciones una persona, considerando que la línea de autobuses “La tortuga” cobra por kilómetro recorrido.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se asignan los valores capturados por consola a las variables correspondientes
    nombre=input(blue+"Ingrese el nombre:\n")
    
    #Se repite si la vraiable start es verdadera
    while start:
        
        #Se capturan los datos y se guardan en las variables flotantes
        presupuesto=float(input(blue+"Ingrese el valor del presupuesto que posee:\n"))
        costo_kilometro=float(input(blue+"Ingrese el costo por kilometro:\n"))
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if presupuesto<=0 or costo_kilometro<=0:
            os.system('cls')
            print(red+"El presupuesto y el costo por kilometro debe ser mayor a 0.")
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #Se define el costo del plan segun el tipo
    costo_mexico= 750*costo_kilometro
    costo_pv= 800*costo_kilometro
    costo_acapulco= 1200*costo_kilometro
    costo_cancun= 1800*costo_kilometro
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if presupuesto >= costo_cancun*2:
        lugar='Cancun'
        costo=costo_cancun
    elif presupuesto >= costo_acapulco*2 and presupuesto < costo_cancun*2:  
        lugar='Acapulco'
        costo=costo_acapulco
    elif presupuesto >= costo_pv*2 and presupuesto < costo_acapulco*2:  
        lugar='P.V'    
        costo=costo_pv
    elif presupuesto >= costo_mexico*2 and presupuesto < costo_pv*2:  
        lugar='Mexico'    
        costo=costo_mexico
    else:
        lugar='casa'
        print(green+f"Hola {nombre} tienes un presupuesto de: ${presupuesto}.\n") 
        print(green+f"El lugar mas barato para viajar es Mexico con un costo de ida y vuelta de: ${costo_mexico*2}.\n")
        print(green+f"Te recomiendo quedarte en {lugar}") 
        costo=0   
    
    if lugar!='casa':    
        print(green+f"Hola {nombre} tienes un presupuesto de ${presupuesto}, puedes viajar a {lugar}.\n")
    if costo!=0:
        print(green+f"El costo del pasaje de ida es de: ${costo}\n")  
        print(green+f"El costo del pasaje de vuelta es de: ${costo}\n")                     
                          
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      