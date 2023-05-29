"""
Cierta empresa proporciona un bono mensual a sus trabajadores, 
el cual puede ser por su antigüantiguedad o bien por el monto de su 
sueldo (el que sea mayor), de la siguiente forma: 

Cuando la antigüantiguedad es mayor a 2 años pero menor a 5, 
se otorga 20 % de su sueldo; cuando es de 5 años o más, 30 %. 
Ahora bien, el bono por concepto de sueldo, si éste es menor a $1000, 
se da 25 % de éste, cuando éste es mayor a $1000, pero menor o igual a $3500, 
se otorga 15% de su sueldo, para más de $3500. 10%. Realice el algoritmo 
correspondiente para calcular los dos tipos de bono, asignando el mayor, 
y represéntelo con un diagrama de flujo y pseudocódigo.

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
print(green+"Muestra cual es el bono que se debe entregar a los empleados según su antiguantiguedad o sueldo.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
    
    #Se asignan los valores de antiguedad y sueldo a las variables correspondientes
    nombre=input(blue+"Ingrese el nombre del empleado:\n")
    antiguedad=int(input(blue+"Ingrese la antiguantiguedad del empleado:\n"))
    sueldo=float(input(blue+"Ingrese el sueldo alcanzado:\n"))
    
    #Se compara la variable antiguedad y sueldo y se realiza una acción segun cada caso.
    if antiguedad > 2 and antiguedad < 5:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de un bono por ${sueldo*0.20} en total tu pago es de ${sueldo+(sueldo*0.20)}"))
    elif antiguedad>=5:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de un bono por ${sueldo*0.30} en total tu pago es de ${sueldo+(sueldo*0.30)}"))
    elif sueldo < 1000: 
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de un bono por ${sueldo*0.25} en total tu pago es de ${sueldo+(sueldo*0.25)}"))
    elif sueldo > 1000 and sueldo <= 3500:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de un bono por ${sueldo*0.15} en total tu pago es de ${sueldo+(sueldo*0.15)}"))
    elif sueldo > 3500:
        print(green+(f"Felicitaciones {nombre}, has sido merecedor de un bono por ${sueldo*0.10} en total tu pago es de ${sueldo+(sueldo*0.10)}"))
                          
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      