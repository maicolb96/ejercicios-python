from clases.programador import Programador
import os

"""
15.	Crea una clase "Programador" que extienda de la clase 
"Empleado" y que tenga como propiedad adicional "lenguaje". 
El método "calcular_salario_neto" de esta clase debe devolver 
el salario neto del programador, restando impuestos, otros 
descuentos y un bono adicional por ser experto en un lenguaje 
en particular.
"""

os.system('cls')

detalle = {"el nombre":"","el apellido":"","el sueldo":"","el lenguaje":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

programador = Programador(detalle["el nombre"],detalle["el apellido"],detalle["el sueldo"],detalle["el lenguaje"])
salario = programador.calc_salario_neto(0.19,5000)

print("Este algoritmo crea un objeto programador a partir de la instancia de una clase empleado.\n")
print(f"Nombre: {programador.nombre} {programador.apellido}\n"
      f"Lenguaje: {programador.lenguaje}\n"
      f"Salario Neto: {salario}")

