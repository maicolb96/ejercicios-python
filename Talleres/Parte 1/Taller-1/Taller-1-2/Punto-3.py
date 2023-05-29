"""
Un maestro desea saber qué porcentaje de hombres y 
que porcentaje de mujeres hay en un grupo de estudiantes
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')
          
#Se imprime el funcionamiento del algoritmo
print("Este algoritmo calcula el porcentaje de hombres y mujeres en un grupo\n")

#-------------------------------ENTRADAS----------------------------------
#Captura la cantidad total de integrantes del grupo
integrantes=int(input("Ingrese la cantidad total de integrantes del grupo:\n"))
hombres=int(input("Ingrese la cantidad de hombres del grupo:\n"))
mujeres=int(input("Ingrese la cantidad de mujeres del grupo:\n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula el porcentaje de hombres y mujeres en un grupo y se asigna a las variables
porcentaje_mujeres=(mujeres*100)/integrantes
porcentaje_hombres=(hombres*100)/integrantes


#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("El grupo tiene ",integrantes," integrantes de los cuales el ",porcentaje_hombres,"% son hombres y el ",porcentaje_mujeres,"% son mujeres.\n")
