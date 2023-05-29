#Se importa la libreria os que permite utilizar 
#varias funciones propias del sistema operativo
import os

"""
Formula de intensidad de corriente
Donde (I) intensidad de corriente Q (Carga electrica) (T) tiempo
"""

"""
El siguiente algoritmo calcula la intensidad de corriente,
la carga electríca y el tiempo.
"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa permite calcular la (I) intensidad de corriente Q (Carga electrica) (T) tiempo.\n ")

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
                    "Ingrese 1 para Intensidad de Corriente (I)\n"
                    "Ingrese 2 para Carga Eléctrica (Q)\n"
                    "Ingrese 3 para Tiempo (T)\n"
                    "Ingrese 4 para Salir\n"
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

        print("Has escogido Intensidad de Corriente (I)\n")

                #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                #Se leen los datos y se almacenan en una variable.
                q=float(input("Ingresde el valor de la carga eléctrica (Q): \n"))
                t=float(input("Ingresde el tiempo (T): \n"))
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
    
        i=q/t
         
        print("La formula de intensidad de corriente es I=Q/T\n")

        print("Aplicandola segun los datos: \nI = ",q," / ",t,"\nI = ",i,"\n")

    elif opc==2:

        print("Has escogido Carga eléctrica (Q)\n")

        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                #Se leen los datos y se almacenan en una variable.
                i=float(input("Ingresde el valor de la intensidad de corriente (I): \n"))
                t=float(input("Ingresde el tiempo (T): \n"))
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
    
        q=t*i
         
        print("La formula de Carga eléctrica es Q=T*I\n")

        print("Aplicandola segun los datos: \nQ = ",t," * ",i,"\nQ = ",q,"\n")

    elif opc==3:

        print("Has escogido Tiempo (T)\n")

        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                #Se leen los datos y se almacenan en una variable.
                i=float(input("Ingresde el valor de la intensidad de corriente (I): \n"))
                q=float(input("Ingresde el valor de la carga eléctrica (Q): \n"))
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
    
        t=q/i
         
        print("La formula de Carga eléctrica es T=Q/I\n")

        print("Aplicandola segun los datos: \nT = ",q," / ",i,"\nT = ",t,"\n")

    elif opc==4:
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