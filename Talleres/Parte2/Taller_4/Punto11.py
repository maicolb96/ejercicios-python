from clases.rectangulo import Rectangulo
import os

"""
11.	Crea una clase "Rectangulo" que extienda de la clase 
"Forma" y que tenga como método adicional "calcular_perimetro"
que devuelva el perímetro del rectángulo.
"""

os.system('cls')

detalle = {"el ancho":"","el alto":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

rectangulo = Rectangulo(detalle["el ancho"],detalle["el alto"])
area = rectangulo.calc_area()
perimetro = rectangulo.calc_perimetro()

print("Este algoritmo crea un objeto Rectangulo a partir de la instancia de una clase Forma.\n")
print(f"Área del rectangulo: {area}\nPerimetro del rectangulo: {perimetro}")

