from clases.vehiculo import Vehiculo
import os

"""
1.	Define una clase "Vehiculo" que tenga como propiedades 
"marca", "modelo" y "año". También debe tener un método 
"obtener_info" que muestre la información del vehículo.
"""

os.system('cls')

detalle = {"la marca":"","el modelo":"","el año":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

carro = Vehiculo(detalle["la marca"],detalle["el modelo"],detalle["el año"])
info = carro.obtener_info()

print("Este algoritmo crea un objeto vehiculo a partir de la instancia de una clase vehiculo.\n")
print("Información del vehiculo")
for key in info.keys(): print(f"{key}: {info[key]}")
