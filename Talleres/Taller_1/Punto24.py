from package.Functions import *

def copy_document(name):
    lineas=read_document("agenda.csv",1)
    if not os.path.isfile(sources_directory(name)):
        with open(sources_directory(name), "w", encoding="utf-8") as document:
            for linea in lineas:
                document.writelines(linea)
        print(f"El documento agenda.csv ha sido copiado con el nomre {name}.")
    else:
        print(f"El documento {name} ya existe.")    

cls()
print("Este algoritmo copia el archivo sources/agenda.csv en la misma ruta relativa.")
new_name=input("Ingrese el nuevo nombre para el archivo y su extensión:\n")
cls()
copy_document(new_name)


