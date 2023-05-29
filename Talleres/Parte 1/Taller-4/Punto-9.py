""" 
Una estación, climática proporciona un par de temperaturas 
diarias (máxima, mínima) (no es posible que alguna o ambas 
temperaturas sea 9 grados): La pareja fin de temperatura es 0,0. 
Se pide determinar el número de días, cuyas temperaturas se han 
proporcionado, la media máxima y mínima, el número de errores. 

–Temperatura de 9°
–Y el porcentaje que representaban.
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
# Inicializar las variables contadoras y acumuladores
dias_sin_error = 0
dias_con_error = 0
temp_max_array=[]
temp_min_array=[]
sum_max = 0
sum_min = 0
errores = 0
count=0

def calculate_media():
    
    global sum_max,sum_min, errores

    # Calcular la media de las temperaturas
    if dias_sin_error > 0:
        media_maximas = sum_max / dias_sin_error
        media_minimas = sum_min / dias_sin_error
    
        # Calcular el porcentaje de errores
        porcentaje_errores = (errores / (dias_sin_error + errores)) * 100
    
        # Imprimir los resultados
        print(msg.format_message('INFx025',temp_max_array,None,None))
        print(msg.format_message('INFx026',temp_min_array,None,None))
        print(msg.format_message('INFx027',dias_sin_error,dias_con_error,None))
        print(msg.format_message('INFx028',dias_con_error,None,None))
        print(msg.format_message('INFx029',dias_sin_error,None,None))
        print(msg.format_message('INFx030',media_maximas,None,None))        
        print(msg.format_message('INFx031',media_minimas,None,None)) 
        print(msg.format_message('INFx032',errores,porcentaje_errores,None)) 
    else:
        print(msg.format_message('INFx033',None,None,None))
    exit()    

def count_sum(temperatura_maxima,temperatura_minima):
  
  global dias_sin_error, dias_con_error,sum_max,sum_min, errores, temp_max_array, temp_min_array
  
  temp_max_array.append(temperatura_maxima)
  temp_min_array.append(temperatura_minima)

  if temperatura_maxima == 0 and temperatura_minima == 0:
     calculate_media() 
  if temperatura_maxima == 9 or temperatura_minima == 9:
      dias_con_error += 1
      errores += 1
  else:
      dias_sin_error += 1
      sum_max += temperatura_maxima
      sum_min += temperatura_minima

def main():
    
    global count
    
    while True:
        count+=1

        #Mensaje que dice de que es el algoritmo
        print(msg.format_message('INFx023',None,None,None))

        # Obtener las temperaturas del usuario
        print(msg.format_message('INFx024',None,None,None))

        temperatura_maxima = float(input(msg.format_message('INPx013',count,None,None)))
        temperatura_minima = float(input(msg.format_message('INPx014',count,None,None)))
        os.system('cls')
        count_sum(temperatura_maxima,temperatura_minima)

main()

                

