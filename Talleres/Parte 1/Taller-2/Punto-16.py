"""
Realice un algoritmo que permitan determinar qué paquete
 se puede comprar una persona con el dinero que recibirá 
 en diciembre, considerando lo siguiente: 

• Paquete A. Si recibe $50,000 o más se comprará una televisión, 
  un modular, tres pares de zapatos, cinco camisas y cinco pantalones. 

• Paquete B. Si recibe menos de $50,000 pero más (o igual) de $20,000,
  se comprará una grabadora, tres pares de zapatos, cinco camisas y 
  cinco pantalones. 

• Paquete C. Si recibe menos de $20,000 pero más (o igual) de $10,000, 
  se comprará dos pares de zapatos, tres camisas y tres pantalones. 

• Paquete D. Si recibe menos de $10,000, se tendrá que conformar con un 
  par de zapatos, dos camisas y dos pantalones.

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
print(green+"Determina que paquetes se pueden comprar con el dinero de Diciembre.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se repite si la vraiable start es verdadera
    while start:
        
        #Se capturan los datos y se guardan en las variables flotantes
        presupuesto=float(input(blue+"Ingrese el presupuesto:\n"))
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if presupuesto<0:
            os.system('cls')
            print(red+"El presupuesto no puede ser menor a cero.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if presupuesto >= 50000: 
        paquete="Paquete A: Una televisión, un modular, tres pares de zapatos, cinco camisas y cinco pantalones."
    elif presupuesto >=20000 and presupuesto < 50000:
        paquete="Paquete B: Una grabadora, tres pares de zapatos, cinco camisas y cinco pantalones."
    elif presupuesto >=10000 and presupuesto < 20000:
        paquete="Paquete C: Dos pares de zapatos, tres camisas y tres pantalones."
    elif presupuesto < 10000:
        paquete="Paquete D: Un par de zapatos, dos camisas y dos pantalones."    
             
            
    
    print(green+f"Como tu presupuesto es de ${presupuesto}, puedes comprar el {paquete}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      