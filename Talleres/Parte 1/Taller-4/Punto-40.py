"""
Se desea conocer una serie de datos de una empresa con  50 empleados:  
a-Cuántos empleados  se ganan más de 300.000 pesetas al mes. (Salarios altos)
b-Entre 100.000 y 300.000 pesetas. (Salarios medios)
c-menos de 100.000 pesetas (Salarios bajos y empleados a tiempo parcial)

"""
import os
os.system("cls")

print("Este algoritmo cuenta los empleados segun sus ganancias.\n")

suma_altos=0
suma_medios=0
suma_bajos=0

for i in range(50):
    os.system("cls")
    sueldo=float(input(f"Ingrese el sueldo del trabajador #{i+1}: "))

    if sueldo>300000:suma_altos+=1
    elif sueldo<=300000 and sueldo>=100000:suma_medios+=1
    elif sueldo<100000:suma_bajos+=1

os.system("cls")
print(f"El número de empleados con sueldo alto (más de 300.000 pesetas) es: {suma_altos}\n"
      f"El número de empleados con sueldo medio (entre 100.000 y 300.000 pesetas) es: {suma_medios}\n"
      f"El número de empleados con sueldo bajo (menos de 100.000 pesetas) es: {suma_bajos}\n"
      )