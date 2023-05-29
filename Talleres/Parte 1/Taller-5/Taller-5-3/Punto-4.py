"""
Hacer un vector 1 x 10, cuyo contenido sea las tablas de 
multiplicar del 9, solo puedes ingresar el número 9 y el 1 
para calcular la tabla, el algoritmo debe calcular los demás
números por si solo, ¿Cómo lo harías?

Claves:
Recuerda que una multiplicación es la una suma; ejemplo
2*1=2
2*2=4
2*3=6
2*4=8
Porque la multiplicación es una suma:
2=2
2+2= 4
2+2+2=6
2+2+2+2=8
Ahora tienes más idea como hacer el algoritmo.
"""

import os
os.system("cls")

tabla_del_9 = [9 * (i+1) for i in range(10)]

print(tabla_del_9)