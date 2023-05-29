"""
En la biblioteca de la facultad de ingeniería, 
se quiere almacenar en un vector de 10 elementos 
8 grandes áreas o disciplinas, en orden alfabético, 
para ello se requiere construir un programa que permita 
insertar las áreas y además los libros que pertenezcan a 
cada una de ellas para el año 2014. El algoritmo debe 
presentar la cantidad de libros en cada una de las áreas, 
además de un rango entre las cantidades mínimas y máximas 
adquiridas durante el año 2014 en cada disciplina. 

Los contenidos sucesivos del vector son los siguientes: 
1 Algoritmia 
2 Estructuras 
3 Física 
4 Cálculo 
5 Programación estructurada 
6 Algebra lineal 
7 Lenguajes de programación 
8 Redes 
9 
10 

"""
import os
os.system("cls")

libros_por_area = [[], [], [], [], [], [], [], []] 

nombres_areas = ["Algoritmia", 
                 "Estructuras", 
                 "Física", 
                 "Cálculo", 
                 "Programación estructurada", 
                 "Algebra lineal", 
                 "Lenguajes de programación", 
                 "Redes"]

for i in range(len(nombres_areas)):  
    print("Ingrese la cantidad de libros para", nombres_areas[i], "en el año 2014:")
    n_libros = int(input())
    libros_por_area[i] = [nombres_areas[i], n_libros]  

os.system("cls")
for area in libros_por_area:  
    print("La cantidad de libros en", area[0], "es", area[1])
    
    if area[1] == 0: 
        continue
    
    print("El rango de cantidad de libros adquiridos en", area[0], "durante el año 2014 es entre", area[1], "y", area[1]*10)
