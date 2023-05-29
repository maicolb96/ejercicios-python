#Se importa la libreria os que permite utilizar 
#varias funciones propias del sistema operativo
import os

"""
Formula de velocidad
Donde (V) es velocidad D es distancia y (T) tiempo
"""

"""
El siguiente algoritmo calcula la velocidad,
la distancia y el tiempo que recorre un objeto.
"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa permite calcular la velocidad (V), la distancia (D) y el tiempo (T) que recorre un objeto.\n ")

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
                    "Ingrese 1 para Velocidad (V)\n"
                    "Ingrese 2 para Distancia (D)\n"
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

        print("Has escogido Velocidad (V)\n")

                #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                #Se leen los datos y se almacenan en una variable.
                d=float(input("Ingresde el valor de la distancia en m: \n"))
                t=float(input("Ingresde el tiempo en s: \n"))
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
    
        v=d/t
         
        print("La formula de velocidad es V=D/T\n")

        print("Aplicandola segun los datos: \nV = ",d," / ",t,"\nV = ",v," m/s\n")

    elif opc==2:

        print("Has escogido Distancia (D)\n")

        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                #Se leen los datos y se almacenan en una variable.
                v=float(input("Ingresde el valor de la velocidad en m/s: \n"))
                t=float(input("Ingresde el tiempo en s: \n"))
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
    
        d=t*v
         
        print("La formula de Distancia es D=V*T\n")

        print("Aplicandola segun los datos: \nD = ",v," * ",t,"\nD = ",d," m\n")

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
                v=float(input("Ingresde el valor de la velocidad en m/s: \n"))
                d=float(input("Ingresde el valor de la distancia en m: \n"))
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
    
        t=d/v
         
        print("La formula de Carga eléctrica es T=D/V\n")

        print("Aplicandola segun los datos: \nT = ",d," / ",v,"\nT = ",t,"\n")

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