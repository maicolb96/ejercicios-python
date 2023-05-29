"""
Calcular el promedio de 50 valores almacenados en un vector. 
Determinar además cuantos son mayores que el promedio e imprimir
el promedio, el número de datos mayores que el promedio y una lista 
de valores mayores que el promedio.
"""
import os, random
os.system("cls")

# Crear un vector con 50 valores aleatorios entre 0 y 100
vector = [random.randint(0, 100) for _ in range(50)]

# Calcular el promedio
promedio = sum(vector) / len(vector)

# Determinar cuántos valores son mayores que el promedio y cuáles son
mayores_promedio = [valor for valor in vector if valor > promedio]
num_mayores_promedio = len(mayores_promedio)

# Imprimir los resultados
print(f"El promedio es: {promedio}")
print(f"Hay {num_mayores_promedio} valores mayores que el promedio:")
print(mayores_promedio)
