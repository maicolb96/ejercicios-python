"""
La facultad de ingeniería desea un programa que le 
permita realizar procesos de inscripción de los 
estudiantes a los diplomados uno en seguridad 
informática y otro en desarrollo móvil, para ello 
se cuenta con 2 archivos que poseen 
la siguiente información: 

1. Asignatura.dat: 
   Ordenado por Código de la asignatura, 
   nombre del diplomado, nombre asignatura, 
   intensidad horaria, docente que la orienta 

2. Estudiantes.dat: 
   Ordenado por código del estudiante, 
   nombres completos, documento de identidad 
"""

import os
os.system("cls")
import time

with open(r'Talleres\Taller-5\Taller-5-2\Inscritos.dat', "r") as f:
    inscritos = set(tuple(line.strip().split(",")) for line in f)

# Lectura de los archivos de entrada
with open(r'Talleres\Taller-5\Taller-5-2\Asignatura.dat', "r") as asignaturas_archivo:
    asignaturas = [linea.strip().split(",") for linea in asignaturas_archivo]

with open(r'Talleres\Taller-5\Taller-5-2\Estudiantes.dat', "r") as estudiantes_archivo:
    estudiantes = [linea.strip().split(",") for linea in estudiantes_archivo]

# Definición de los diplomas disponibles
DIPLOMA_SEGURIDAD = "Seguridad Informática"
DIPLOMA_DESARROLLO = "Desarrollo Móvil"

# Definición de las asignaturas por diploma
asignaturas_seguridad = [asignatura for asignatura in asignaturas if asignatura[1] == DIPLOMA_SEGURIDAD]
asignaturas_desarrollo = [asignatura for asignatura in asignaturas if asignatura[1] == DIPLOMA_DESARROLLO]

# Definición de las funciones de inscripción
def inscribir_seguridad(diploma,estudiante, inscritos):
    
    # Verificar si el estudiante ya está inscrito en otro diploma
    if (str(estudiante[1])+":"+diploma) in inscritos:
        print(f"El estudiante {estudiante[1]} ya está inscrito en el diploma.")
        return

    # Inscribir al estudiante en las asignaturas correspondientes al diploma de seguridad
    asignaturas_inscritas = []
    for asignatura in asignaturas_seguridad:
        inscripcion = input(f"¿Desea inscribirse en {asignatura[2]} ({asignatura[3]} horas, orientada por {asignatura[4]})? (s/n) ")
        if inscripcion.lower() == "s":
            asignaturas_inscritas.append(asignatura[0])

    # Registrar la inscripción del estudiante y las asignaturas en las que se inscribió
    print(f"El estudiante {estudiante[1]} se ha inscrito en el diploma de Seguridad Informática en las asignaturas:")
    for codigo_asignatura in asignaturas_inscritas:
        asignatura = [a for a in asignaturas_seguridad if a[0] == codigo_asignatura][0]
        print(f"- {asignatura[2]} ({asignatura[3]} horas, orientada por {asignatura[4]})")
    inscritos.add(str(estudiante[1])+":"+diploma)

def inscribir_desarrollo(diploma,estudiante, inscritos):

    # Verificar si el estudiante ya está inscrito en otro diploma
    if (str(estudiante[1])+":"+diploma) in inscritos:
        print(f"El estudiante {estudiante[1]} ya está inscrito en el diploma.")
        return

    # Inscribir al estudiante en las asignaturas correspondientes al diploma de desarrollo
    asignaturas_inscritas = []
    for asignatura in asignaturas_desarrollo:
        inscripcion = input(f"¿Desea inscribirse en {asignatura[2]} ({asignatura[3]} horas, orientada por {asignatura[4]})? (s/n) ")
        if inscripcion.lower() == "s":
            asignaturas_inscritas.append(asignatura[0])

    # Registrar la inscripción del estudiante y las asignaturas en las que se inscribió
    print(f"El estudiante {estudiante[1]} se ha inscrito en el diploma de Desarrollo Móvil en las asignaturas:")
    for codigo_asignatura in asignaturas_inscritas:
        asignatura = [a for a in asignaturas_desarrollo if a[0] == codigo_asignatura][0]
        print(f"- {asignatura[2]} ({asignatura[3]} horas, orientada por {asignatura[4]})")
    inscritos.add(str(estudiante[1])+":"+diploma)


# Procesamiento de las inscripciones
for estudiante in estudiantes:
    state=True
    # Preguntar al usuario en qué diploma desea inscribirse el estudiante
    while state:
        diploma = input(f"¿En qué diploma desea inscribirse {estudiante[1]} ({DIPLOMA_SEGURIDAD}/{DIPLOMA_DESARROLLO})? ")
    
        # Llamar a la función de inscripción correspondiente
        if diploma == DIPLOMA_SEGURIDAD:
            inscribir_seguridad(diploma,estudiante,inscritos)
            state=False
        elif diploma == DIPLOMA_DESARROLLO:
            inscribir_desarrollo(diploma,estudiante,inscritos)
            state=False
        else:
            print(f"El diploma {diploma} no es válido.")
        
        time.sleep(3)
        os.system("cls")
    

with open(r'Talleres\Taller-5\Taller-5-2\Inscritos.dat', "w") as f:
    for inscrito in inscritos:
        f.write(f"{inscrito}\n")        
