from clases.persona import Persona
import os

"""
7.	Define una clase "Persona" que tenga como propiedades 
"nombre", "apellido" y "edad". También debe tener un método 
"obtener_nombre_completo" que devuelva el nombre completo 
de la persona.
"""

os.system('cls')

detalle = {"los nombres":"","los apellidos":"","la edad":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

persona = Persona(detalle["los nombres"],detalle["los apellidos"],detalle["la edad"])
nombre_apellido = persona.obtener_nombre_completo()

print("Este algoritmo crea un objeto persona a partir de la instancia de una clase Persona.\n")
print(f"Nombre: {nombre_apellido}\nEdad: {persona.edad} años.")

