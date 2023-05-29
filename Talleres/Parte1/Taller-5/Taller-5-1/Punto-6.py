"""
Del ejercicio 5 el algoritmo debe ser capaz de preguntar al usuario el nombre
del estudiante que desee mostrar el promedio.
"""

import os
os.system("cls")

notas_matematicas = []
notas_ingles = []
nombres_estudiantes = []
promedios = []

print("Este algoritmo calcula la nota promedio de 5 estudiantes.\n")
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante #{i+1}: ")
    nombres_estudiantes.append(nombre)

    nota_matematica = float(input("Ingrese la nota de matemáticas: "))
    notas_matematicas.append(nota_matematica)

    nota_ingles = float(input("Ingrese la nota de inglés: "))
    notas_ingles.append(nota_ingles)

    promedio = (nota_matematica + nota_ingles) / 2
    promedios.append(promedio)
    os.system("cls")

print("\nLos nombres ingresados son: ", end=" ")
for i in range(5): print(nombres_estudiantes[i],end=" - ")

indice_maximo_promedio = promedios.index(max(promedios))
print("\nEl estudiante con el promedio más alto es:", nombres_estudiantes[indice_maximo_promedio], "con un promedio de", max(promedios),"\n")

# preguntar al usuario el nombre del estudiante cuyo promedio desea mostrar
nombre_estudiante = input("Ingrese el nombre del estudiante cuyo promedio desea mostrar: \n")
while nombre_estudiante not in nombres_estudiantes:
    nombre_estudiante = input("El nombre del estudiante no es válido. Ingrese un nombre válido: ")

# buscar el índice del nombre del estudiante en la lista de nombres de estudiantes
indice_estudiante = nombres_estudiantes.index(nombre_estudiante)

# mostrar el promedio correspondiente del estudiante
print("El promedio de", nombre_estudiante, "es:", promedios[indice_estudiante])