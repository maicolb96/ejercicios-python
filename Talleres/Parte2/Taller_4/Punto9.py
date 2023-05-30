from clases.profesor import Profesor
import os

"""
9.	Crea una clase "Profesor" que extienda de la clase 
"Persona" y que tenga como propiedad adicional "materia". 
El método "obtener_nombre_completo" de esta clase debe 
devolver el nombre completo del profesor y la materia 
que enseña.
"""

os.system('cls')

detalle = {"los nombres":"","los apellidos":"","la edad":"","la materia":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

profesor = Profesor(detalle["los nombres"],detalle["los apellidos"],detalle["la edad"],detalle["la materia"])
nombre_apellido = profesor.obtener_nombre_completo()

print("Este algoritmo crea un objeto profesor a partir de la instancia de una clase Persona.\n")
print(f"Nombre: {nombre_apellido}\nEdad: {profesor.edad} años.")

