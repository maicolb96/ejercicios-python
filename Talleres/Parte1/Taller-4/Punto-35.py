"""
Dado el nombre de un mes y si el año es, o no es bisiesto, 
deducir el número de días del mes.
"""
import os
os.system("cls")

def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False

def numero_de_dias_en_mes(mes, es_bisiesto):
    
    mes = mes.lower()
    dias_por_mes = {
        "enero": 31,
        "febrero": 29 if es_bisiesto else 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31,
    }
    
    return dias_por_mes.get(mes, None)


def main():
    print("Este algoritmo devuelve el número de días de un mes segun el año.\n")

    año=int(input("Ingrese el año: "))
    mes=input("Ingrese el nombre del mes: ")
    dias=numero_de_dias_en_mes(mes,es_bisiesto(año))

    print(f"El número de días del mes {mes} del año {año} es {dias} días.")

main()