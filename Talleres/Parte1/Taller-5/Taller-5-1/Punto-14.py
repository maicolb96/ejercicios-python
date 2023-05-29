'''
Realizar un algoritmo en python que realice un vector A y B,
y sumarlos, es decir posición uno de a y b sumarse y 
llevarlo a un vector c e imprimir la suma.
'''

import os

# limpia la consola
os.system("cls")

print("Realizar un algoritmo en python que realice un vector A y B,\n"
      "y sumarlos, es decir posición uno de a y b sumarse y\n" 
      "llevarlo a un vector c e imprimir la suma.\n")

# crea el vector A ingresado por el usuario
vector_A = []
for i in range(5):
    num_A = int(input("Ingrese un número para el vector A: "))
    vector_A.append(num_A)

# crea el vector B ingresado por el usuario
vector_B = []
for i in range(5):
    num_B = int(input("Ingrese un número para el vector B: "))
    vector_B.append(num_B)

# suma de los vectores A y B y guardarlos en el vector C
vector_C = []
for i in range(5):
    suma = vector_A[i] + vector_B[i]
    vector_C.append(suma)

# muestra el vector C resultante
print("La suma de los vectores A y B es:", vector_C)
