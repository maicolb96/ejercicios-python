""" 
Un comercio dispone de dos tipos de artículos en fichas 
correspondientes a diversas sucursales con los siguientes campos:

- Código del articulo A o B. 
- Precio unitario del artículo. 
- Numero de artículos. 

La última ficha del archivo de artículos tiene un código de artículo,
una letra X. Se pide: 

- El número de artículos existentes de cada categoría.
- El importe total de los artículos de cada categoría.

"""
#Se importa la librería OS que permite interactuar con el sistem
import os
#Se importa un controlador de mensajes creado por mi
from utils import message 

#Se limpia la consola
os.system('cls')   

#Se instancia la clase Message y se crea un objeto llamado msg
msg = message.Message()

"""Nota, msg permite acceder al metodo format_message de la clase Message
   El cual se encarga de retornar un mensaje estructurado según el código
   Que recibe, además puede recibir hasta 3 argumentos para ser usados
   Como variables concatenadas en el texto.
"""
#Se inicializan las variables contadoras/acumuladoras
num_art_A = 0
num_art_B = 0
importe_A = 0.0
importe_B = 0.0

# Obtener la ruta actual
ruta_actual = os.path.abspath(__file__)

# Construir la ruta al archivo "articulos.txt"
ruta_archivo = os.path.join(os.path.dirname(ruta_actual), "utils", "articulos.txt")

# Abrir el archivo de artículos en modo lectura
with open(ruta_archivo, 'r') as f:
    # Leer el archivo línea por línea
    next(f)
    for linea in f:
        # Dividir la línea en campos separados por comas
        campos = linea.strip().split(',')
        # Obtener los campos relevantes
        codigo = campos[0]
        precio = float(campos[1])
        cantidad = int(campos[2])
        # Actualizar contadores y acumuladores según el código del artículo
        if codigo == 'A':
            num_art_A += cantidad
            importe_A += precio * cantidad
        elif codigo == 'B':
            num_art_B += cantidad
            importe_B += precio * cantidad
        elif codigo == 'X':
            # Si se encuentra la letra X, se termina la lectura del archivo
            break

# Imprimir los resultados
print(msg.format_message('INFx021',num_art_A,importe_A,None))
print(msg.format_message('INFx021',num_art_A,importe_A,None))