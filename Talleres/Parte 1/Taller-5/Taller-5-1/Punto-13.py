'''
Realizar un algoritmo en python que permita hacer un vector de 
30 números y mostrar la suma de los pares y el producto de los 
que son múltiplo de 5.
'''

import os

# limpia la consola
os.system("cls")

print("Realizar un algoritmo en python que permita hacer un vector de\n" 
      "30 números y mostrar la suma de los pares y el producto de los\n" 
      "que son múltiplo de 5.\n")

# crea el vector de 30 números ingresados por el usuario
vector = []
for i in range(30):
    num = int(input(f"{i}) Ingrese un número: "))
    vector.append(num)

# suma de los números pares
suma_pares = 0
for num in vector:
    if num % 2 == 0:
        suma_pares += num

# producto de los números múltiplos de 5
producto_multiplos_5 = 1
for num in vector:
    if num % 5 == 0:
        producto_multiplos_5 *= num

# muestra los resultados
print("La suma de los números pares es:", suma_pares)
print("El producto de los números múltiplos de 5 es:", producto_multiplos_5)
