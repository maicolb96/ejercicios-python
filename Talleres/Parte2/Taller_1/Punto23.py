from package.Functions import *

def reader(document_name):
    try:
        ruta = "c"+(((os.path.dirname(os.path.abspath(__file__))).strip('\\package')).replace('\\','/'))+f'/sources/{document_name}'
    
        with open(ruta, "r", encoding="utf-8") as document:
            lineas=document.readlines()   
            for linea in lineas:
                print(linea.replace(","," - "))
    except:
        return "No existe el archivo en la carpeta sources."
    
cls()
print("Este algoritmo lee un archivo de agenda con 1 o N registros.\n")
reader("agenda.csv")


