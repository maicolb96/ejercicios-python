from clases.gato import Gato
import os

"""
6.	Crea una clase "Gato" que extienda de la clase "Animal" 
y que tenga como propiedad adicional "pelaje". El método 
"hacer_ruido" de esta clase debe mostrar un maullido.
"""

os.system('cls')

detalle = {"el nombre":"","la edad":"","el pelaje":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

gato = Gato(detalle["el nombre"],detalle["la edad"],detalle["el pelaje"])
info = gato.info_animal()

print("Este algoritmo crea un objeto gato a partir de la instancia de una clase Animal.\n")
print("Información del Gato")
for key in info.keys(): print(f"{key}: {info[key]}")
