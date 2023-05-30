from clases.gerente import Gerente
import os

"""
14.	Crea una clase "Gerente" que extienda de la clase 
"Empleado" y que tenga como propiedad adicional 
"departamento". El método "calcular_salario_neto" 
de esta clase debe devolver el salario neto del gerente, 
restando impuestos, otros descuentos y un bono adicional 
por ser gerente.
"""

os.system('cls')

detalle = {"el nombre":"","el apellido":"","el sueldo":"","el departamento":""}
for key in detalle.keys(): detalle[key] = input(f"Ingrese {key}: ")
os.system('cls')

gerente = Gerente(detalle["el nombre"],detalle["el apellido"],detalle["el sueldo"],detalle["el departamento"])
salario = gerente.calc_salario_neto(0.19,5000,200000)

print("Este algoritmo crea un objeto gerente a partir de la instancia de una clase empleado.\n")
print(f"Nombre: {gerente.nombre} {gerente.apellido}\n"
      f"Departamento: {gerente.depto}\n"
      f"Salario Neto: {salario}")

