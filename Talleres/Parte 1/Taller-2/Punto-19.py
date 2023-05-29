"""
Realice un algoritmo para resolver el siguiente problema: 

una fábrica de pantalones desea calcular cuál es el precio final de venta 
y cuánto ganará por los N pantalones que produzca con el corte de alguno 
de sus modelos, para esto se cuenta con la siguiente información:

a) Tiene dos modelos A y B, tallas 30, 32 y 36 para ambos modelos. 
b) Para el modelo A se utiliza 1.50 m de tela, y para el B 1.80 m. 
c) Al modelo A se le carga 80 % del costo de la tela, por mano de obra. 
   Al modelo B se le carga 95 % del costo de la tela, por el mismo concepto.
d) A las tallas 32 y 36 se les carga 4 % del costo generado por mano de obra y tela, 
   sin importar el modelo. 
e) Cuando se realiza el corte para fabricar una prenda sólo se hace de un solo modelo y una sola talla. 
f) Finalmente, a la suma de estos costos se les carga 30%, que representa la ganancia extra de la tienda.

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
print(green+"Determina que tipo de vacuna debe aplicarse a una persona.\n")
    
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
        modelo=input(blue+"Ingrese el modelo A o B:\n")
        costo_metro_tela=float(input(blue+"Ingrese el costo por metro de tela:\n"))
        talla=input(blue+"Ingrese la talla:\n")
        
        #verifica si los valores ingresados son menores o iguales a cero. Si no sale del ciclo.
        if costo_metro_tela<0:
            os.system('cls')
            print(red+"El costo de la tela no puede ser menor a 0.") 
        else:
            start=False    
    
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    if talla==32 or talla==36:
        costo_por_talla=costo_metro_tela*0.04
    else:
        costo_por_talla=0

    if modelo=="A" or modelo=="a":
        metro_tela=1.50
        costo_tela=metro_tela*costo_metro_tela
        costo_por_mano=costo_tela*0.80
    elif modelo=="B" or modelo=="ab": 
        metro_tela=1.80
        costo_tela=metro_tela*costo_metro_tela
        costo_por_mano=costo_tela*0.95

    costo_total=costo_por_talla+costo_tela+costo_por_mano
    ganancia=costo_total*0.30
    precio_venta=costo_total+ganancia

    print(green+f"El modelo {modelo}, en la talla {talla}, cuesta fabricarlo ${costo_total}, se debe vender a ${precio_venta} para tener una ganancia de ${ganancia}")
   
except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")

      