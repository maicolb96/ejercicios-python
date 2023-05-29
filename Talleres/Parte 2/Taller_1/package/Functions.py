import csv
import os, time

def cls():
    os.system("cls")

def sleep(t):
    time.sleep(t)   

def read_document(document_name,type):
    lineas=[]
    try:
        ruta = "c"+(((os.path.dirname(os.path.abspath(__file__))).strip('\\package')).replace('\\','/'))+f'/sources/{document_name}'
    
        with open(ruta, "r", encoding="utf-8") as document:
            if type==1: 
                lineas = document.readlines()
            elif type==2: 
                lector=csv.reader(document)      
                for registro in lector:
                    lineas.append(registro) 
        return lineas 
    except:
        return "No existe el archivo en la carpeta sources."
    
def sources_directory(document_name):
    ruta = "c"+(((os.path.dirname(os.path.abspath(__file__))).strip('\\package')).replace('\\','/'))+f'/sources/{document_name}'
    return ruta