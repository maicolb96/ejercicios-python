from clases.automovil import Automovil
import os

"""
2.	Crea una clase "Automovil" que extienda de la clase 
"Vehiculo" y que tenga como propiedad adicional 
"numero_puertas". El método "obtener_info" de esta clase 
debe mostrar la información del automóvil, incluyendo el 
número de puertas.
"""
os.system('cls')

detalle = {"la marca":"","el modelo":"","el año":"","cantidad de puertas":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

auto = Automovil(detalle["la marca"],detalle["el modelo"],detalle["el año"],detalle["cantidad de puertas"])
info = auto.obtener_info()

print("Este algoritmo crea un objeto automovil heredando los atributos de un vehiculo.\n")
print("Información del automovil")
for key in info.keys(): print(f"{key}:{info[key]}")