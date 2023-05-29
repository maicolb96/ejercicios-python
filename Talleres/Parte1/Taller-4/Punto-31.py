"""
Que aceleración tiene un tren que parte de México a (n) km/hrs 
y pasa por Tijuana una hora después a 50 km/hr.
"""

import os
os.system("cls")

print("Este algoritmo calcula la aceleración que tiene un tren que\n" 
      "parte de México a (n) km/hrs y pasa por Tijuana una hora \n"
      "después a 50 km/hr.\n")

vel_inicial=float(input("Ingrese la velocidad inicial: "))
vel_final=50

print(f"La aceleración del tren es de: {(vel_final-vel_inicial)/1}Km/h^2")