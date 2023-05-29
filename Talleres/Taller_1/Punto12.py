from package.Functions import *

"""
12.Escribir una función que permita deducir 
si una fecha leída del teclado es válida.
"""

def validate_ano_bis(ano):
    if ano%4==0 and ano%100==0 and ano%400==0: return True
    else: return False

def validate_date(date):
    try:
        separator= "-" if "-" in date else "/"
        d,m,a = map(int,date.split(separator))
        ano_bis = validate_ano_bis(a)
        
        if a<=0 or d<=0 or d>31 or m<=0 or m>12: return False
        elif m==2 and ano_bis and d>29 or m==2 and not ano_bis and d>28: return False
        elif m in [4,6,9,11] and d>30: return False
        else: return True
    except:
        return False    

print("Este algoritmo recibe una fecha y verifica si es correcta.\n")
while True: 
    cls()
    date=input("Ingrese una fecha en formato dd/mm/aaaa o dd-mm-aa:\n")
    if validate_date(date):print(f"La fecha {date} es válida.");break
    else:print(f"La fecha {date} es invalida.")
    sleep(2)



