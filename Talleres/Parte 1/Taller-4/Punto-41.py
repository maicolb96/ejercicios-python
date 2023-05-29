"""
Ingresar las N notas de las materias de un estudiante en un vector y calcular: 
a) cuantas notas no ha aprobado, 
b) cuantas ha aprobado, 
c) promedio de las notas, 
d) promedio de notas aprobadas y desaprobadas.

"""

import os

cant_aprobadas=0
cant_no_aprobadas=0
suma_aprobadas=0
suma_no_aprobadas=0
notas=[]
i=0

while True:
    os.system("cls")
    print("Este algoritmo lee las calificaciones de un estudiante\n" 
      "y calcula notas aprobadas, no aprobadas, promedio de\n" 
       "aprobadas y promedio de no aprobadas (aprobada mayor o igual a 5).\n")

    print("Ingrese las notas, escriba 20 para terminar.\n")

    i+=1
    nota=float(input(f"Ingrese la nota #{i}: "))

    if nota!=20: notas.append(nota)
    else: break

print("\nNotas: "+((str(notas).replace(","," - ")).replace("[","")).replace("]","")) 

for item in notas:
    if item>=5: cant_aprobadas+=1;suma_aprobadas+=item 
    elif item<5: cant_no_aprobadas+=1;suma_no_aprobadas+=item

print(f"Cantidad de notas totales: {len(notas)}\n"
      f"Cantidad de notas aprobadas: {cant_aprobadas}\n"
      f"Cantidad de notas no aprobadas: {cant_no_aprobadas}\n"
      f"Promedio de notas totales: {suma_aprobadas+suma_no_aprobadas/len(notas)}\n"
      f"Promedio de notas aprobadas: {suma_aprobadas/len(notas)}\n"
      f"Promedio de notas no aprobadas: {suma_no_aprobadas/len(notas)}\n"
      )
