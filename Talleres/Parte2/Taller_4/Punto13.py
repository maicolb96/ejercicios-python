from clases.empleado import Empleado
import os

"""
13.	Define una clase "Empleado" que tenga como propiedades 
"nombre", "apellido" y "sueldo". También debe tener un método 
"calcular_salario_neto" que devuelva el salario neto del 
empleado, restando impuestos y otros descuentos.
"""

os.system('cls')

detalle = {"el nombre":"","el apellido":"","el sueldo":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

empleado = Empleado(detalle["el nombre"],detalle["el apellido"],detalle["el sueldo"])
salario = empleado.calc_salario_neto(0.19,5000)

print("Este algoritmo crea un objeto empleado a partir de la instancia de una clase Empleado.\n")
print(f"Nombre: {empleado.nombre} {empleado.apellido}\n"
      f"Salario Neto: {salario}")

