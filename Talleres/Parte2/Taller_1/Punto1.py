import numpy as np
#Se importa un paquete propio que tiene algunas funciones simplificadas
from package.Functions import cls

"""
Diseñar una función que calcule la 
media de tres números leídos del 
teclado y poner un ejemplo de su aplicación.
"""
#Esta función toma un vector como entrada y calcula la media de sus elementos
def media(vect):
    return np.mean(vect) 

#Esta función solicita al usuario que ingrese n números y los almacena en una lista llamada "vector"
def reader(n):
    vector=[int(input(f"Ingrese el #{i} número: "))for i in range(1,n+1,1)]    
    return vector

#Llama a la función personalizada "cls" para limpiar la pantalla
cls()

#solicita al usuario que ingrese la cantidad de números que desea promediar
n=input("¿Cuantos números va a promediar?\n") 

#Llama la funcion media para obtener la media y pasa el vector retornado de reader
media=media(reader(int(n)))

#Imprime el resultado de la media calculada
print(f"\nEl promedio de los números ingresados es de: {media}")
