from clases.estudiante import Estudiante
import os

"""
8.	Crea una clase "Estudiante" que extienda de la clase 
"Persona" y que tenga como propiedad adicional "carrera". 
El método "obtener_nombre_completo" de esta clase debe 
devolver el nombre completo del estudiante y su carrera.
"""

os.system('cls')

detalle = {"los nombres":"","los apellidos":"","la edad":"","la carrera":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

estudiante = Estudiante(detalle["los nombres"],detalle["los apellidos"],detalle["la edad"],detalle["la carrera"])
nombre_apellido = estudiante.obtener_nombre_completo()

print("Este algoritmo crea un objeto Estudiante a partir de la instancia de una clase Persona.\n")
print(f"Nombre: {nombre_apellido}\nEdad: {estudiante.edad} años.")

