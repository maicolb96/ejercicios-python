from clases.animal import Animal
import os

"""
4.	Define una clase "Animal" que tenga como propiedades 
"nombre" y "edad". También debe tener un método "hacer_ruido" 
que muestre un mensaje genérico.
"""

os.system('cls')

detalle = {"el nombre":"","la edad":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

animal = Animal(detalle["el nombre"],detalle["la edad"])
info = animal.info_animal()

print("Este algoritmo crea un objeto animal a partir de la instancia de una clase Animal.\n")
print("Información del Animal")
for key in info.keys(): print(f"{key}: {info[key]}")
