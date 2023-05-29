from package.Functions import *
import Punto1 as p1
"""
20. Crea una lista llamada ordenada con los elementos de la lista números ordenados de menor a mayor utilizando el método sort().

"""

cls()
print("Este algoritmo crea una lista llamada ordenada con los elementos de la lista números ordenados de menor a mayor utilizando el método sort().")

"""Si se quier usar sort() no se puede guardar en una lista o variable
Puesto que su retorno es None ya que el ordena la lista directamente
En la lista original"""

#Por eso primero se ordeno la lista 
p1.numeros.sort()

#Luego se imprime
print(p1.numeros)

#Si lo que quiere es ordenrla y retornar 
#la lista ordenada para guardarla en una variable 
#se debe usar sorted(lista)

ordenada = sorted(p1.numeros)

#Luego se imprime
print(ordenada)