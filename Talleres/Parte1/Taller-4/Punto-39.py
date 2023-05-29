"""
Se desea leer las calificaciones de una clase de 
informática y contar el número total de aprobados 
(5 o mayor que 5).
"""

import os
os.system("cls")

print("Este algoritmo lee las calificaciones de una clase\n" 
      "de informática y contar el número total de aprobados\n" 
       "(5 o mayor que 5)\n")

integrantes=int(input("Ingrese el numero de estudiantes: "))

suma=0

#for i in range(integrantes):
#    os.system("cls")
#    nota=float(input(f"Ingrese la nota del estudiante #{i+1}: "))
#    if nota>=5:
#        suma+=1

nota=[float(input(f"Ingrese la nota del estudiante #{i+1}: ")) for i in range(integrantes)]
suma = [1 for item in nota if item>=5]

os.system("cls")
print(suma)
print(f"El número de estudiantes aprobados es: {len(suma)}\n"
      f"El número de estudiantes reprobados es: {integrantes-int(len(suma))}")