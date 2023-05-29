from numpy import mean
from package.Functions import *

"""
17.dado el nombre de una serie de estudiantes y las 
calificaciones obtenidas en un examen, calcular e 
imprimir la calificación media así como cada calificación
y la diferencia con la media.
"""

def print_notas(est,notas):
    for nombre,nota in zip(est,notas):
        print(f"La nota de {nombre} es: {nota}")
        print(f"La nota {nota} menos la media {mean(notas)} es: {nota-mean(notas)}\n")

cls()

estudiantes=[]
notas=[]

print("Este programa calcula la media de las notas de un examen de n estudiantes.\n")
n=int(input("Ingrese la cantidad de estudiantes a registrar:\n"))
cls()

for i in range(n):
    estudiantes.append(input(f"Ingrese el nombre del estudiante #{i+1}:\n"))
    notas.append(int(input(f"Ingrese la nota de {estudiantes[i]}:\n")))
    cls()
   
print(f"\nLa media de las notas ingresadas por los estudiantes es: {mean(notas)}\n")
print_notas(estudiantes,notas)
