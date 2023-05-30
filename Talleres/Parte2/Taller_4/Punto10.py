from clases.forma import Forma
import os

"""
10.	Define una clase "Forma" que tenga como propiedades 
"ancho" y "alto". También debe tener un método 
"calcular_area" que devuelva el área de la forma.
"""

os.system('cls')

detalle = {"el ancho":"","el alto":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

figura = Forma(detalle["el ancho"],detalle["el alto"])
area = figura.calc_area()

print("Este algoritmo crea un objeto figura a partir de la instancia de una clase Forma.\n")
print(f"Área de la figura: {area}")

