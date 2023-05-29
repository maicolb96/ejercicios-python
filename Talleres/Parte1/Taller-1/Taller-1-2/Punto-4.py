"""
Se desea saber cuántos pinos y cuantos cedros se pueden sembrar 
en un terreno que miden cantidad de metros. El dueño ha establecido 
que sembrará el 35% del terreno en pinos y el 65% en cedros. 
Las normas de agricultura establecen que en 10 metros cuadrados 
se pueden sembrar 4 pinos y en 15 metros cuadrados 5 cedros.
"""
#Se imprime el funcionamiento del algoritmo
print("Este algoritmo calcula la cantidad de pinos y cedros que se pueden cembrar en un terreno de x tamaño")

#-------------------------------ENTRADAS----------------------------------
#Captura el área en metros cuadrados y se guarda en una variable flotante
area_terreno=float(input("Ingrese el área en metros cuadrados del terreno\n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula el área disponible para pinos y cedros y se guarda en sus respectivas variables
area_pinos=0.35*area_terreno
area_cedros=0.65*area_terreno

#10m 4pinos - 15m 5cedros

#Se calcula la cantidad de pinos y cedros y se asigna el valor a su respectiva variable
cantidad_pinos=(area_pinos/10)*4
cantidad_cedros=(area_cedros/15)*5

#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("El área destinada para sembrar pinos es de ",area_pinos," metros cuadrados\nPuedes sembrar ",cantidad_pinos," pinos.")
print("El área destinada para sembrar cedros es de ",area_cedros," metros cuadrados\nPuedes sembrar ",cantidad_cedros," cedros.")