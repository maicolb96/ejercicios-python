from package.Functions import *

"""
12.	Modifica el valor de la clave "edad" del diccionario persona.
"""

cls()
persona = {
            "Nombre" : 'Michael Blandón',
            "Edad" : 26,
            "Ciudad" : 'Medellín'
        }

print("Este algoritmo modifica el valor de la clave edad del diccionario persona.")
persona["Edad"] = 33
print(persona)