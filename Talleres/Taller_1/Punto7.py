import math
from package.Functions import *

"""
Realizar un procedimiento que realice la conversión 
de coordinadas polares(r,0) a coordenadas caterianas x,y
X= r. cos(0)
Y= r. sen(0)
"""

def covert_point():
    return (r*math.cos(a),r*math.sin(a))

cls()

print("Este algoritmo convierte coordenadas polares a coordenadas cartesianas.")
r=float(input("Ingrese la distancia radial r: \n"))
a=float(input("Ingrese el angulo: \n"))

print(f"La coordenada polar {r,a} corresponde a la coordenada cartesiana {covert_point()}")