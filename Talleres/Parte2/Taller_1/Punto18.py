from package.Functions import *

def count_letters(lineas,archivo):
    a=0; an=0; aand=0
    for linea in lineas:
        palabras=linea.split()
        for palabra in palabras:
            if "A" in palabra.upper():a+=1 
            if "AN" in palabra.upper():an+=1
            if "AND" in palabra.upper():aand+=1        
    
    print(f"Hay {a} a en el archivo {archivo}.")
    print(f"Hay {an} an en el archivo {archivo}.")
    print(f"Hay {aand} and en el archivo {archivo}.")

cls()
try:
    while True:
        print("Recuerde guardar previamente el archivo en la carpeta sources.\n")
        archivo=input("Ingrese el nombre del archivo con su extensión: \n")
        lineas=read_document(archivo,1)
        cls()
        if not "No existe" in lineas:
            count_letters(lineas,archivo)
            break
        else: 
            print(lineas)
except ValueError as e:
    print(e)