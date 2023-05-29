from automovil import Automovil
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
print(auto.obtener_info())