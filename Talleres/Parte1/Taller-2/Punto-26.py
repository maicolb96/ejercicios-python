"""
Realice el algoritmo para determinar cuánto pagará una persona
 que adquiere N artículos, los cuales están de promoción. 
 Considere que si su precio es mayor o igual a $200 se le 
 aplica un descuento de 15%, y si su precio es mayor a $100 
 pero menor a $200, el descuento es de 12%; de lo contrario, 
 sólo se le aplica 10%. Se debe saber cuál es el costo y el 
 descuento que tendrá cada uno de los artículos y finalmente 
 cuánto se pagará por todos los artículos obtenidos.
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
print(green+"Este algoritmo determina cuánto pagará una persona que adquiere N artículos, los cuales están de promoción.\n")
    
"""
Try
Verifica si hay errores en la ejecución, en try se ejecuta
el código sin errores.
Except
En except se ejecuta el código cuando hay un error.
"""
try:
        
    #Se capturan los datos y se guardan en las variables flotantes
    cantidad = int(input(blue+"Ingrese la cantidad de articulos a comprar: \n"))
    precio1=0; precio2=0; precio3=0
    suma1=0; suma2=0; suma3=0
    #Utiliza la función system para limpiar la consola
    os.system('cls')
    
    #se verifica segun el presupuesto a que lugar puede viajar
    for i in range(cantidad):

        precio=float(input(f"Ingrese el precio del articulo {i+1}: "))

        if precio>=200:
            precio1=(precio-(precio*0.15))
            suma1=suma1+precio1
            print(f'Este articulo tiene un precio de ${precio} y tien un descuento de 15% que equivale a '+str(precio*0.15)+f' debe pagar ${precio1} por éste artículo.\n')
        elif precio>100 and precio<200:
            precio2=(precio-(precio*0.12))
            suma2=suma2+precio2
            print(f'Este articulo tiene un precio de ${precio} y tien un descuento de 12% que equivale a '+str(precio*0.12)+f' debe pagar ${precio2} por éste artículo.\n')
        else:
            precio3=(precio-(precio*0.10))
            suma3=suma3+precio3
            print(f'Este articulo tiene un precio de ${precio} y tien un descuento de 10% que equivale a '+str(precio*0.10)+f' debe pagar ${precio3} por éste artículo.\n')
    
    print(green+f"\nEl valor a pagar por todos los articulos es de: ${suma1+suma2+suma3}")

except ValueError as e:
    os.system('cls')
    print(red+f"Ha ocurrido un error, vuelva a ingresar los datos: {e}\n")


      

      

      

      