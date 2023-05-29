from package.Functions import *
import csv

def modify_agenda(registros,idRegistro):

    if idRegistro < 1 or idRegistro > len(registros):
        print("El número de registro ingresado no es válido.")
    elif "No existe" in registros:
        print(registros)    
    else:
        cls()
        registro_actual = registros[idRegistro]
        print(f"Registro #{idRegistro}:\n")
        for r,ra in zip(registros[0],registro_actual): print(f"{r}: {ra}")
        print("\n")
        items = ["Nombre","Dirección","Ciudad","Código Postal","Teléfono","Edad"]
        nuevo_registro = []
        for i in range(6): nuevo_registro.append(input(f"Ingrese el nuevo valor para {items[i]}: "))
        cls()
        print("El registro ha sido modificado exitosamente.\n")
        registros[idRegistro] = nuevo_registro
        for registro in registros:
                var=str(registro).replace(", "," | ").replace("'","").replace("[","").replace("]","")
                print(var)
    

        with open(sources_directory("agenda.csv"), "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            for registro in registros:
                escritor.writerow(registro)
    


cls()
idRegistro = int(input("Ingrese el número de registro que desea modificar: "))
registros=read_document("agenda.csv",2)
modify_agenda(registros,idRegistro)


