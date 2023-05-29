#Se importa la libreria os que permite utilizar 
#varias funciones propias del sistema operativo
import os
#Se importa la libreria math para usar barias funciones matemáticas
import math
"""
Puntos del 38 al 43
Realizar el siguiente listado de fórmulas algoritmos independientes, 
donde el usuario digite el valor década termino.
"""

"""
El siguiente algoritmo calcula velocidad final, velocidad inicial,
tiempo, aceleración y fuerza.
"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa permite calcular velocidad final, velocidad inicial, tiempo, aceleración y fuerza\n ")

#Se crea un ciclo que se repite hasta que su estado sea cambiado
while True:

    #Se define una variable verdadera para entrar en un ciclo 
    state=True

    #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
    #cuando se ingresa una opción valida numérica
    while state==True:

        #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
        try:
            #Se lee un valor por consola y se asigna a una variable entera
            opc=float(input(
                    "Ingrese 1 para aceleración a = V/t\n"
                    "Ingrese 2 para aceleración a = Vf - Vi/t\n"
                    "Ingrese 3 para velocidad final\n"
                    "Ingrese 4 para velocidad inicial\n"
                    "Ingrese 5 para fuerza\n"
                    "Ingrese 6 para masa\n"
                    "Ingrese 7 para aceleración a=f/m\n"
                    "Ingrese 6 para Salir\n"
                    "\n"
                    ))
            state=False
        #Utilizamos except para manejar los errores y guardamos el valor del error
        # en una variable e    
        except ValueError as e:
            #Limpiamos la consola
            os.system('cls')
            #Verificamos si el error corresponde a una entrada erronea como una cadena
            if "could not convert string to float:" in str(e):
                print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
            
    
    #Limpiamos la consola
    os.system('cls')
    
    #Este if verifica la opcion que el usuario ingresó y se guardo en la variable opc
    if opc==1:
        
        print("Has seleccionado aceleración a = V/t\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                v=float(input("Ingrese la velocidad en m/s\n"))
                t=float(input("Ingrese el tiempo en s\n"))
                
                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')

                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
    
        a=v/t
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de aceleración es a = V/t\n")

        print("Aplicandola segun los datos: \na = ",v," / ",t,"\na = ",a,"\n")    
    
    elif opc==2:
        
        print("Has seleccionado aceleración a = Vf-Vi/T\n ")
        
         #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                vf=float(input("Ingrese la velocidad final en m/s\n "))
                vi=float(input("Ingrese la velocidad inicial en m/s\n "))
                t=float(input("Ingrese el tiempo en s\n "))
                
                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')

                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
        
        a=(vf-vi)/t
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de aceleración es a = Vf-Vi/t\n")

        print("Aplicandola segun los datos: \na = (",vf," - ",vi,")/",t,"\na = ",a,"\n")  

    elif opc==3:

        print("Has seleccionado velocidad final\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                vi=float(input("Ingrese la velocidad inicial m/s\n "))
                a=float(input("Ingrese la aceleracion en m/s^2\n "))
                t=float(input("Ingrese el tiempo en s\n "))

                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')
             
                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
    
        vf=vi+(a*t)
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de velocidad final es vf = vi + (a*t)\n")

        print("Aplicandola segun los datos: \nvf = ",vi," + (",a," * ",t,")\nvf = ",vf,"\n")  

    elif opc==4:

        print("Has seleccionado velocidad inicial\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                vf=float(input("Ingrese la velocidad final m/s\n "))
                a=float(input("Ingrese la aceleracion en m/s^2\n "))
                t=float(input("Ingrese el tiempo en s\n "))

                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')
             
                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
    
        vi=vf-(a*t)
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de velocidad final es vi = vf - (a*t)\n")

        print("Aplicandola segun los datos: \nvi = ",vf," - (",a," * ",t,")\nvi = ",vi,"\n")               
    
    elif opc==5:

        print("Has seleccionado Fuerza\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                a=float(input("Ingrese la aceleracion en m/s^2\n "))
                m=float(input("Ingrese la masa en kg\n"))

                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')

                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
        
        f=a*m
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de fuerza es F = a*m\n")

        print("Aplicandola segun los datos: \nF = ",a," * ",m,"\nF = ",f,"\n")

    elif opc==6:

        print("Has seleccionado masa\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                a=float(input("Ingrese la fuerza en m/s^2\n "))
                f=float(input("Ingrese la masa en N\n"))

                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')

                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
        
        m=f/a
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de masa es m = f/a\n")

        print("Aplicandola segun los datos: \nm = ",f," / ",a,"\nm = ",m,"\n")  

    elif opc==7:

        print("Has seleccionado aceleración\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa en kg\n "))
                f=float(input("Ingrese la masa en N\n"))

                state=False

            #Utilizamos except para manejar los errores y guardamos el valor del error
            #en una variable e     
            except ValueError as e:
                #Limpiamos la consola
                os.system('cls')

                #Verificamos si el error corresponde a una entrada erronea como una cadena
                if "could not convert string to float:" in str(e):
                    print("Ingrese una opción valida (Recuerde ingresar numeros no letras)\n")
    
        #Limpiamos la consola
        os.system('cls')
        
        a=f/m
    
        #Muestra paso a paso la resolución de la formula
        print("La formula de masa es a = f/m\n")

        print("Aplicandola segun los datos: \na = ",f," / ",m,"\na = ",a,"\n")   
    
    elif opc==8:
        #Limpiamos la consola
        os.system('cls')
        print("Has salido del programa")
        exit()

    #Se define una variable verdadera para entrar en un ciclo 
    state=True

    #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
    #cuando se ingresa una opción valida numérica
    while state==True:
        #Verificar si desea calcular otra figura
        recal=input("Ingrese 1 para continuar ó Ingrese 2 para salir\n")
        
        if recal=='2':
            #Limpiamos la consola
            os.system('cls')
            print("Has salido del programa")
            exit()
        elif recal=='1':
            state=False
            #Limpiamos la consola
            os.system('cls') 
        else:
            print("Ingrese una opción valida")                 