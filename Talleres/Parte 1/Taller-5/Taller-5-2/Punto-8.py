"""
Realice un Algoritmo que teniendo en cuenta los 
siguientes datos de entrada:

- Cod. De Cliente
- Tipo de Cuenta (Ahorro, Corriente)
- Tipo de Actualización (Aporte, Retiro)* Monto de la Transacción

Calcule y de cómo salida lo siguiente:

- Monto Total de Aporte en Ahorro
- Monto Total de Retiro en Corriente
- Promedio de Retiro en Ahorro.
"""

import os
os.system("cls")

print("Algoritmo para calcular el monto total de\n" 
      "aporte en ahorro, monto total de retiro en\n" 
      "corriente y promedio de retiro en ahorro\n" 
      "de una entidad financiera.\n")

monto_aporte_ahorro = 0
monto_retiro_corriente = 0
total_retiro_ahorro = 0
cantidad_retiro_ahorro = 0

cod_cliente = input("Ingrese el código de cliente: ")
tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro/Corriente): ")
tipo_actualizacion = input("Ingrese el tipo de actualización (Aporte/Retiro): ")
monto_transaccion = float(input("Ingrese el monto de la transacción: "))

if "horro" in tipo_cuenta and "porte" in tipo_actualizacion:
    monto_aporte_ahorro += monto_transaccion
elif "orriente" in tipo_cuenta and "etiro" in tipo_actualizacion:
    monto_retiro_corriente += monto_transaccion
    if "horro" in tipo_cuenta:
        total_retiro_ahorro += monto_transaccion
        cantidad_retiro_ahorro += 1

print("Monto total de aporte en Ahorro: ", monto_aporte_ahorro)
print("Monto total de retiro en Corriente: ", monto_retiro_corriente)
if cantidad_retiro_ahorro > 0:
    promedio_retiro_ahorro = total_retiro_ahorro / cantidad_retiro_ahorro
    print("Promedio de retiro en Ahorro: ", promedio_retiro_ahorro)
else:
    print("No hubo retiros en cuenta de Ahorro.")

