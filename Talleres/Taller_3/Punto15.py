from package.Functions import *

"""
15.	Crea una lista llamada valores con todos los valores del diccionario persona.
"""

cls()
valores = []
persona = {
            "Nombre" : 'Michael Blandón',
            "Edad" : 26,
            "Ciudad" : 'Medellín'
        }

for key in persona.values(): valores.append(key)

print("Este algoritmo crea una lista llamada valores con todos los valores del diccionario persona.")
print(valores)