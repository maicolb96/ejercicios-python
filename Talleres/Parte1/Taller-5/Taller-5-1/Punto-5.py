import os
os.system("cls")

"""
Hacer en python un vector donde el usuario ingrese 5 nota matemáticas, otro vector 5
notas inglés y el vector nombre del estudiante al que corresponde dichas notas,
de esos vectores debe calcular un vector promedio, más adelante vector
promedio debe mostrar todos los promedios y el estudiante que corresponda.
"""

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

for i in range(5):
    print("El promedio de", nombres_estudiantes[i], "es:", promedios[i])

indice_maximo_promedio = promedios.index(max(promedios))
print("El estudiante con el promedio más alto es:", nombres_estudiantes[indice_maximo_promedio], "con un promedio de", max(promedios))
