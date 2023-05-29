from package.Functions import *

"""
Diseñar un procedimiento que acepte un numero de mes,
un numero de día y un numero de año y los visualice en 
el formato dd/mm/aa Por ejemplo, los valores 19,09,1987 
se visualizarían así: 19/9/87 y para los valores 3,9, 
y 1905 así: 3/9/05.
"""

#Función que le da formato a la fecha
def formatDate():
    format_date=""
    for i in date: format_date+= i+"/" if date.index(i)<(len(date)-1) else i[2:]
    return format_date

#Se limpia pantalla
cls()

#Se guardan frases en un arreglo para reciclar texto
item=["el día","el mes","el año"]

#Se crea un array con el dia, mes y año
date = [input(f"Ingrese {item[i]}: \n") for i in range(3)]

#Se llama la función de formateo y se imprime la fecha formateada
print(f"\nLa fecha ingresada es: {formatDate()}\n")