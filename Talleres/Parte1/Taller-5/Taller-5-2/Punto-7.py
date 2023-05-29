"""
Un Tecnológico, ofrece un curso “x” y desea realizar un 
algoritmo que permita determinar y dar como salida la 
cantidad de dinero recaudado por concepto del curso; 
teniendo en cuenta que se tiene por cada participante 
la siguiente información:

- Cedula de Identidad
- Nombre del Participante
- Procedencia:
    At = Alumno del Tecnológico, 
    Dt = Docente del Tecnológico, 
    Pg = Publico en General).

Tomando en cuenta que la procedencia se cobra de 
la siguiente tarifa:

- At = 10.000 pesos
- Dt = 20.000 pesos.
- Pg = 35.000 pesos.

"""
import os
os.system("cls")

print("Este es un Algoritmo para calcular el dinero recaudado por un curso en un tecnológico.\n")

num_participantes = int(input("Ingrese el número de participantes: "))

total_recaudado = 0

for i in range(num_participantes):
    os.system("cls")
    ci = input(f"Ingrese la cédula de identidad del participante {i+1}: ")
    nombre = input(f"Ingrese el nombre del participante {i+1}: ")
    procedencia = input(f"Ingrese la procedencia (At, Dt o Pg) del participante {i+1}: ")

    if procedencia == "At":
        costo = 10000
    elif procedencia == "Dt":
        costo = 20000
    else:
        costo = 35000

    total_recaudado += costo

os.system("cls")
print(f"El total recaudado por el curso es: {total_recaudado} pesos.")
