"""
Diseñe un algoritmo que almacene en un vector 
llamado FIB [100] los 100 primeros números 
de la serie Fibonacci.
"""

import os
os.system("cls")

print("El algoritmo almacena en un vector llamado FIB [100] los 100 primeros números de la serie Fibonacci.\n")

fib=[0,1]

for i in range (2,101,1):
    fib.append(fib[i-1]+fib[i-2])

print(fib)

