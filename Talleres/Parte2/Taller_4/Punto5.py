from clases.perro import Perro
import os

"""
5.	Crea una clase "Perro" que extienda de la clase 
"Animal" y que tenga como propiedad adicional "raza". 
El método "hacer_ruido" de esta clase debe mostrar un ladrido.
"""

os.system('cls')

detalle = {"el nombre":"","la edad":"","la raza":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

perro = Perro(detalle["el nombre"],detalle["la edad"],detalle["la raza"])
info = perro.hacer_ruido()

print("Este algoritmo crea un objeto perro a partir de la instancia de una clase Animal.\n")
print("Información del Perro")
for key in info.keys(): print(f"{key}: {info[key]}")
