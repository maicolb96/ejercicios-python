from package.Functions import *

"""13.escribir el algoritmo que permita obtener el número de elementos positivos de
una tabla."""

def leer_tabla():
    cols=int(input("Ingrese el número de columnas que tendrá la tabla:\n"))
    rows=int(input("Ingrese el número de filas que tendrá la tabla sin tener en cuenta la fila de titulos:\n"))
    cls()
    mat= [[f"V{j+1}" if i==0 else input(f"Ingrese el valor {i,j}:\n") for j in range(cols)]for i in range(rows+1)]
    return mat
    
def print_tabla(matriz): 
    cls() 
    mat=matriz
    for m in mat:
        if mat.index(m) == 0: print("--TABLA--")
        for i in m:
            print(i, end=" ")
        print() 

def verify_negative(mat):
    neg = []
    count = 0
    for row in mat:
        for value in row:
            try:
                if int(value)<0: neg.append(int(value)); count+=1
            except:1==1
    print(f"Los negativos son {neg} y son en total {count} negativos.")


try:
    cls()
    print("Este algoritmo lee los datos de una tabla y busca valores negativos.\n")
    table=leer_tabla()
    print_tabla(table)  
    verify_negative(table) 
except ValueError as e:
    print(e)    