"""
Elaborar un algoritmo para que calcule la nota definitiva 
de un estudiante de lógica, se debe leer las siguientes 
notas por pantalla: seguimiento 60%, I parcial 20%, 
II parcial 20%; al final debe imprimir un mensaje que 
indique si ganó o perdió la materia.
"""
#Importa la libreria os, consular documentación de python
import os

#Se limpia la consola
os.system('cls')

#Se imprime el funcionamiento del algoritmo
print("El algoritmo calcula la nota definitiva de un estudiante a partir de las notas parciales e indica si aprobó.\n")

#-------------------------------ENTRADAS----------------------------------

#Captura las notas parciales
seguimiento=float(input("Ingrese la nota de seguimiento (60%): \n"))
parcial1=float(input("Ingrese la nota del parcial 1 (20%): \n"))
parcial2=float(input("Ingrese la nota del parcial 2 (20%): \n"))

#-------------------------------PROCESOS----------------------------------
#Se calcula la nota definitiva segun los porcentajes.
nota_final=(0.6*seguimiento)+(0.2*parcial1)+(0.2*parcial2)

#Se verifica si el mes de nacimiento esta por encima o por debajo del mes actual
if nota_final>=3.5:
    #Se imprimen los resultados SALIDAS
    print("Tu nota final es de ",nota_final,"¡Felicitaciones, has aprobado la competencia!")
else:
    #Se imprimen los resultados SALIDAS
    print("Tu nota final es de ",nota_final,"Lo sentimos, debes validar la competencia.") 

