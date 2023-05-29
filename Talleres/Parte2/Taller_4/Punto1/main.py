from vehiculo import Vehiculo
from package.Functions import cls

"""
1.	Define una clase "Vehiculo" que tenga como propiedades 
"marca", "modelo" y "año". También debe tener un método 
"obtener_info" que muestre la información del vehículo.
"""

cls()

carro = Vehiculo("Toyota","Supra","2023")
info = carro.obtener_info()

print("Información del carro")
for key in info.keys(): print(f"{key}: {info[key]}")