"""
Un estudiante desea saber a partir de sus notas parciales, 
la definitiva en la asignatura de programación, teniendo 
en cuenta que esta se califica de la siguiente forma: 
un seguimiento que equivale al 40%, un parcial que 
equivale al 20% un proyecto que equivale al 10% 
y un final que equivale al 30%.
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("Este algoritmo calcula la nota final a partir de las notas parciales y sus porcentajes\n")

#-------------------------------ENTRADAS----------------------------------
#Captura las notas parciales
seguimiento = float(input("Ingrese la nota de seguimiento (40%):\n"))
parcial = float(input("Ingrese la nota del parcial (20%):\n"))
proyecto = float(input("Ingrese la nota del proyecto (10%):\n"))
final = float(input("Ingrese la nota del final (30%):\n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula la nota final
nota_final = (seguimiento*0.4) + (parcial*0.2) + (proyecto*0.1) + (final*0.3)

#-------------------------------SALIDAS----------------------------------
#Se imprimen los resultados
print("La nota final es: ",nota_final)

