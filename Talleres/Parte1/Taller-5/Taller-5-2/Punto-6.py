"""
Una Ferretería vende dos tipos de Cables, Cable Tipo A 
(200 Bs. MT) y Cable Tipo B (300 Bs. MT ); realice un 
algoritmo que teniendo como datos por cada cliente su 
nombre, tipo de cable a comprar y cantidad de metros 
requeridos, calcule y de cómo salida el nombre y el 
neto a pagar por cada cliente, tomando en cuenta 
que existe un grupo indeterminado de ellos y que la 
empresa da una rebaja del 10% por cada compra que exceda 
de los 100 MT de cable de cualquier tipo.
"""
import os
os.system("cls")


num_clientes = int(input("Ingrese el número de clientes: "))

netos_a = []
netos_b = []


for i in range(num_clientes):
    os.system("cls")
    nombre = input(f"Ingrese el nombre del cliente {i+1}: ")
    tipo_cable = input(f"Ingrese el tipo de cable a comprar (A o B) para el cliente {i+1}: ")
    metros = float(input(f"Ingrese la cantidad de metros de cable a comprar para el cliente {i+1}: "))

    precio = 200 if tipo_cable == "A" else 300
    neto = precio * metros

    if metros > 100:
        neto *= 0.9

    if tipo_cable == "A":
        netos_a.append(neto)
    else:
        netos_b.append(neto)

    print(f"El cliente {nombre} debe pagar un neto de {neto} Bs.")

os.system("cls")
total_a = sum(netos_a)
total_b = sum(netos_b)
print(f"Total vendido de Cable A: {total_a} Bs.")
print(f"Total vendido de Cable B: {total_b} Bs.")

