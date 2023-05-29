"""
Un alumno desea saber cuál será su calificación final 
en la materia de Algoritmos. Dicha calificación se compone 
de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.

"""
import os
import numpy as np

os.system("cls")
print("Este algoritmo calcula el promedio de la materia de algoritmos de un estudiante.\n")

parciales=[]
examen=0
trabajo=0

for i in range(5):
   if i <= 2:
      parciales.append(float(input(f"Ingrese la nota parcial {i+1}: ")))
   elif i==3:
      examen=float(input("Ingrese la nota del examen final: "))
   else:
      trabajo=float(input("Ingrese la nota del trabajo final: ")) 

os.system("cls")

print(f"Promedio parciales: {np.mean(parciales)}\n"
      f"Nota del exámen final: {examen}\n"
      f"Nota del trabajo final: {trabajo}\n"
      f"Nota final de la materia: {((np.mean(parciales)*0.55)+examen*0.30+trabajo*0.15):.2f}")