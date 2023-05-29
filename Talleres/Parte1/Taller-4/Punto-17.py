"""
Un estudiante desea saber cuál será su promedio general 
en las tres materias más difíciles que cursa y cuál será 
el promedio que obtendrá en cada una de ellas. 

Estas materias se evalúan como se muestra a continuación:

Asignatura | Examen | Cantidad de Tareas | Porcentaje de Tareas

Matemáticas    90%            3                     10%
Física         80%            2                     20%
Química        85%            3                     15%
"""

import os
os.system("cls")

task=[]
materias=["Matemáticas","Física","Quimica"]
state=[]
printer=[]
prom_tot=0
def print_result():
    for item in printer:
        print(item)
    exit()

def calculate(mat,n):
    global task, prom_tot
    sum_math=0
    sum_exam=0
    count=0
    for item in task:
        count+=1
        if mat in item:
            if count!=(n+1): 
                sum_math+=int(str(item).replace(mat,""))
            else:
                sum_exam+=int(str(item).replace(mat,""))  
    printer.append(f"El promedio para {mat} es de: {((sum_math*0.10)/n)+(sum_exam*0.9)}")
    prom_tot+=((sum_math*0.10)/n)+(sum_exam*0.9)
    task=[]
    if len(state)>=2:
        printer.append(f"El promedio total es de: {prom_tot/3}")
        print_result()
def capture_note(opc,n):
    global task
    if opc not in state:
        for i in range(n+1):
            if i<n: task.append(materias[int(opc)-1]+input(f"Ingrese la nota de la tarea {i+1} de {materias[int(opc)-1]}:\n")) 
            elif i==n: task.append(materias[int(opc)-1]+input(f"Ingrese la nota del exámen de {materias[int(opc)-1]}:\n")) 
        os.system("cls")
        calculate(materias[int(opc)-1],n)
    else:
        os.system("cls")
        print(f"Ya ingresaste las notas para {materias[int(opc)-1]}.\n")       

print("Este algoritmo calcula su promedio para las siguientes materias, y el promedio total.\n")

while True:
    opc=input("Ingrese 1 para Matemáticas\nIngrese 2 para Física\nIngrese 3 para Quimica\n")
    
    if opc=="1":
        capture_note(opc,3)
        if opc not in state:state.append(opc)
    elif opc=="2": 
        capture_note(opc,2)
        if opc not in state:state.append(opc)
    elif opc=="3": 
        capture_note(opc,3);
        if opc not in state:state.append(opc)
    
    
 
    

