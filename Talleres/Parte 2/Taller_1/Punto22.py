import csv
from package.Functions import *

"""
22.diseñar un algoritmo que permita crear un 
archivo Agenda de direcciones cuyos registros 
constan de los siguientes campos

a) Nombre dirección
b) Ciudad
c) Código
d) postal
e) Teléfono
f) edad
"""

def create_agenda():
    agenda = []
    data = ["Nombre","Dirección","Ciudad","Código Postal","Teléfono","Edad"]
    count = 0
    while True:
        count+=1

        print(f"Ingrese los datos para el registro #{count}.\n")

        registro = {}
        for i in range(6): registro[data[i]]=input(f"Ingrese {data[i]}: ")

        agenda.append(registro)
        
        cls()

        print("¡Registro agregado correctamente!\n")
        respuesta = input("¿Desea agregar otro registro? (S/N) ")
        if respuesta.lower() != "s": break

        cls()
    
    if not os.path.isfile(sources_directory("agenda.csv")):
        with open(sources_directory("agenda.csv"), "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Dirección", "Ciudad", "Código Postal", "Teléfono", "Edad"])
            escritor.writeheader()
            for registro in agenda: escritor.writerow(registro)
    else:
        with open(sources_directory("agenda.csv"), "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Dirección", "Ciudad", "Código Postal", "Teléfono", "Edad"])
            for registro in agenda: escritor.writerow(registro)
    
cls()
print("Este algoritmo crea un archivo de agenda con 1 o N registros.\n")
create_agenda()


