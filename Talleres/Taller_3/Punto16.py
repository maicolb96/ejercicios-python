from package.Functions import *
import Punto14 as p14
import Punto15 as p15

"""
16.	Crea una lista llamada pares con todos los pares clave-valor del diccionario persona.

"""

cls()
pares = []
persona = {
            "Nombre" : 'Michael Blandón',
            "Edad" : 26,
            "Ciudad" : 'Medellín'
        }

claves = p14.claves
valores = p15.valores

for c,v in zip(claves, valores):
    pares.append(f"{c}: {v}")

print("Este algoritmo crea una lista llamada pares con todos los pares clave-valor del diccionario persona.")
print(pares)