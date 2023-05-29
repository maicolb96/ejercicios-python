from package.Functions import *

"""
13.	Elimina la clave "ciudad" del diccionario persona.
"""

cls()
persona = {
            "Nombre" : 'Michael Blandón',
            "Edad" : 26,
            "Ciudad" : 'Medellín'
        }

print("Este algoritmo elimina la clave ciudad del diccionario persona.")
persona.pop("Ciudad", None)
print(persona)