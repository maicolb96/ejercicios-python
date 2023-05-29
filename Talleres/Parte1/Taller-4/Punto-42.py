"""
Un teatro otorga descuentos según la edad del cliente. Determinar 
la cantidad de dinero que el teatro deja de percibir por los niños 
menores de 5 años, además se pide presentar la cantidad de personas 
registradas, clasificadas por categorías. 

Al final se presentan las edades de las personas.
 Categoría		Edad		Descuento
	1		    0-5		       50%
	2		    Mayor 5-40     25%
    3	        Mayor 40- 	   10%
"""
import os
os.system("cls")

ninos = 0
categoria1 = 0
categoria2 = 0
categoria3 = 0
dinero_perdido = 0

edades = []

print("Un teatro otorga descuentos según la edad del cliente. Determinar\n" 
      "la cantidad de dinero que el teatro deja de percibir por los niños \n"
      "menores de 5 años, además se pide presentar la cantidad de personas \n"
      "registradas, clasificadas por categorías.\n"
      )

costo=float(input("Ingrese el costo de la boleta: "))
while True:
    edad = input("Ingrese la edad de la persona (o 'salir' para terminar): ")
    if edad == 'salir':
        break
    
    edad = int(edad)
    edades.append(edad)
    
    if edad <= 5:
        ninos += 1
        dinero_perdido += 0.5
        categoria1 += 1
    elif edad <= 40:
        categoria2 += 1
        dinero_perdido += 0.25
    else:
        categoria3 += 1
        dinero_perdido += 0.1

os.system("cls")
print(f"Cantidad de personas registradas en la categoría 1: {categoria1}")
print(f"Cantidad de personas registradas en la categoría 2: {categoria2}")
print(f"Cantidad de personas registradas en la categoría 3: {categoria3}")
print(f"Dinero perdido por los niños menores de 5 años: ${dinero_perdido*costo}")
print(f"Edades registradas: {edades}")


