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
auto = Automovil("Chevi","Spark",2019,4)
info = auto.obtener_info()

print("Información del automovil")
for key in info.keys(): print(f"{key}:{info[key]}")