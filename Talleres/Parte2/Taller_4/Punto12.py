from clases.circulo import Circulo
import os

"""
12.	Crea una clase "Circulo" que extienda de la clase "Forma" 
y que tenga como método adicional "calcular_circunferencia" 
que devuelva la circunferencia del círculo.
"""

os.system('cls')


radio = input("Ingrese el radio del circulo: ")
os.system('cls')

circulo = Circulo(radio)
area = circulo.calc_area()
circunferencia = circulo.calc_circunferencia()

print("Este algoritmo crea un objeto circulo a partir de la instancia de una clase Forma.\n")
print(f"Área del circulo: {area}\nCircunferencia del circulo: {circunferencia}")

