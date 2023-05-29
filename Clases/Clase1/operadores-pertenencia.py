#Operadores de Pertenencia

"""
   Este es un ejemplo de uso de los operadores
   de pertenencia in - not in que buscan una coincidencia
   en una cadena o arreglo

"""
#Funcion que determina si un caracter existe en una cadena.
def existOnChain():

    #Se crea y asigna valor a la cadena 
    cadena = input("Ingrese una palabra: \n") 
    #Se crea y asigna valor al caracter
    caracter = input("Ingrese un caracter a buscar en la cadena: \n") 

    if caracter in cadena: # compara si el caracter esta en (in) la cadena
        print("El caracter "+caracter+" esta en la cadena "+cadena)

    if caracter not in cadena: # compara si el caracter no esta en (not in) la cadena  
        print("El caracter "+caracter+" no esta en la cadena "+cadena) 

#Funcion que determina si un caracter existe en un arreglo.
def existOnArray():

    #Se crea un arreglo constante.
    array=[1,2,3,4,5,6,7,8,9]
    #Se crea y asigna valor al caracter
    caracter = input("Ingrese un número a buscar en el arreglo: \n") 

    if int(caracter) in array: # compara si el caracter esta en (in) la cadena
        print("El caracter "+caracter+" esta en el arreglo ",array)

    if int(caracter) not in array: # compara si el caracter no esta en (not in) la cadena  
        print("El caracter "+caracter+" no esta en el arreglo ",array) 

#Método principal
def main():
    
    #Informa que hace el programa
    print("Este programa identifica si un caracter existe en una cadena de texto")
    #Muestra un pequeño menu que hace algo según la opción
    opc=input("Ingrese 1 para buscar en una cadena\nIngrese 2 para buscar en un arreglo:\n")
    
    #Compara la opción ingresada con un valor
    if opc=='1': 
        #Se llama al metodo que busca el caracter en la cadena y se le pasan los parametros
        existOnChain()
    elif opc=='2':
        #Se llama al metodo que busca el caracter en el arreglo y se le pasan los parametros
        existOnArray()

main()    