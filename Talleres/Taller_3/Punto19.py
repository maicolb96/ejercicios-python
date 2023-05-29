from package.Functions import *

"""
19. Crea un diccionario llamado personas con los nombres y edades de varias personas. Luego, crea una lista llamada mayores con los nombres de las personas mayores de edad (mayores o iguales a 18 años).

"""

cls()
personas = {
    "Nombres":["Juan", "Rosa", "Liliana","Mathias"],
    "Edades":[17, 54, 33, 14]
}

mayores = []

for edad, name in zip(personas["Edades"],personas["Nombres"]):
    if edad >= 18:
        mayores.append(f"{name}: {edad}")

print("Este algoritmo crea un diccionario llamado personas con los nombres y edades de varias personas. Luego, crea una lista llamada mayores con los nombres de las personas mayores de edad (mayores o iguales a 18 años).")
print(mayores)