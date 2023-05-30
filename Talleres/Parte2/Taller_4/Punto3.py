from clases.camioneta import Camioneta
import os

"""
3.	Crea una clase "Camioneta" que extienda de la clase 
"Vehiculo" y que tenga como propiedad adicional 
"capacidad_carga". El método "obtener_info" de esta 
clase debe mostrar la información de la camioneta, 
incluyendo la capacidad de carga.
"""
os.system('cls')

detalle = {"la marca":"","el modelo":"","el año":"","la capacidad de carga":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

camioneta = Camioneta(detalle["la marca"],detalle["el modelo"],detalle["el año"],detalle["la capacidad de carga"])
info = camioneta.obtener_info()

print("Este algoritmo crea un objeto camioneta heredando los atributos de un vehiculo.\n")
print("Información del automovil")
for key in info.keys(): print(f"{key}:{info[key]}")