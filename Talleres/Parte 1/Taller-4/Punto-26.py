"""
Un maestro desea saber qué porcentaje de hombres 
y que porcentaje de mujeres hay en un grupo de estudiantes.
"""

import os
os.system("cls")

print("Este algoritmo muestra el porcentaje de hombres y mujeres en un grupo.\n")

hombres=(int(input("Ingrese la cantidad de hombres en el grupo: \n")))
mujeres=(int(input("Ingrese la cantidad de mujeres en el grupo: \n")))

print(f"Total de integrantes: {hombres+mujeres}\n"
      f"Total hombres: {hombres}\n"
      f"Total mujeres: {mujeres}\n"
      f"Porcentaje hombres: {(hombres/(hombres+mujeres))*100}%\n"
      f"Porcentaje mujeres: {(mujeres/(hombres+mujeres))*100}%\n"
      )