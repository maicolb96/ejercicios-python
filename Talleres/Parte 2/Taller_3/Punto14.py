from package.Functions import *

"""
14.	Crea una lista llamada claves con todas las claves del diccionario persona.
"""

cls()
claves = []
persona = {
            "Nombre" : 'Michael Blandón',
            "Edad" : 26,
            "Ciudad" : 'Medellín'
        }

for key in persona.keys(): claves.append(key)

print("Este algoritmo crea una lista llamada claves con todas las claves del diccionario persona.")
print(claves)