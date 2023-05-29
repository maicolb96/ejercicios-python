from clases.vehiculo import Vehiculo
import os

"""
1.	Define una clase "Vehiculo" que tenga como propiedades 
"marca", "modelo" y "año". También debe tener un método 
"obtener_info" que muestre la información del vehículo.
"""

os.system('cls')
carro = Vehiculo("Toyota","Supra","2023")
info = carro.obtener_info()

print("Información del vehiculo")
for key in info.keys(): print(f"{key}: {info[key]}")
