from package.Functions import *

"""
18. Crea una lista llamada cuadrados con los cuadrados de los números del 1 al 5 utilizando una lista por comprensión.

"""

cls()
cuadrados = [i**2 for i in range (1,6,1)]
print("Este algoritmo crea una lista llamada cuadrados con los cuadrados de los números del 1 al 5 utilizando una lista por comprensión.")
print(cuadrados)