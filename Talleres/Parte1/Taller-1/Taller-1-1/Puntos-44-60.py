#Se importa la libreria os que permite utilizar 
#varias funciones propias del sistema operativo
import os
#Se importa la libreria math para usar barias funciones matemáticas
import math
"""
Punto C
Realizar el siguiente listado de fórmulas algoritmos independientes, 
donde el usuario digite el valor década termino.
"""

"""
El siguiente algoritmo el área y volúmen de diferentes 
figuras a través de su formula algebraica.
"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa permite calcular el área y volúmen de algunas figuras\n ")

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
                    "Ingrese 1 para Energia Cinetica\n"
                    "Ingrese 2 para Energia Potencial\n"
                    "Ingrese 3 para Densidad\n"
                    "Ingrese 4 para Presion\n"
                    "Ingrese 5 para Fuerza de presion\n"
                    "Ingrese 6 para Area de presion\n"
                    "Ingrese 7 para Presión Hidrostática\n"
                    "Ingrese 8 para Densidad en presión hidrostática\n"
                    "Ingrese 9 para altura o profundidad en presión hidrostática\n"
                    "Ingrese 10 para Calor\n"
                    "Ingrese 11 para Calor Específico\n"
                    "Ingrese 12 para Temperatura Final\n"
                    "Ingrese 13 para Temperatura Inicial\n"
                    "Ingrese 14 para Salir\n"
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
        
        print("Has seleccionado Energia Cinetica\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa en kg\n"))
                v=float(input("Ingrese velocidad en m/s\n"))
                
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
    
        ec=1/2(m*(v**2))
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Energía Cinetica: EC = 1/2 M*V^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- EC = 1/2(",m," * (",v,"^2)")
        print("- EC = 0.5(",m," * ",v**2)
        print("- EC = 0.5 * ",m*(v**2))
        print("- EC = ",ec,"\n")   
    
    elif opc==2:
        
        print("Has seleccionado Energia Potencial\n ")
        
         #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa en kg\n "))
                g=float(input("Ingrese la grabedad en m/s^2\n "))
                h=float(input("Ingrese la altura en m\n "))
            
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
        
        ep=m*g*h
    
         #Muestra paso a paso la resolución de la formula
        print("Ecuación de Energia Potencial: EP = M*g*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- EP = ",m," * ",g," * ",h)
        print("- EP = ",ep,"\n")
    

    elif opc==3:

        print("Has seleccionado Densidad\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa en g\n "))
                v=float(input("Ingrese el volumen en m^3\n "))

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
    
        d=m/v
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de la Densidad: D = M/V\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- D = ",m," / ",v)
        print("- D = ",d,"\n")

    elif opc==4:

        print("Has seleccionado Presión\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                f=float(input("Ingrese la fuerza en N\n "))
                a=float(input("Ingrese el área en m^2\n "))

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
        
        p=f/a
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de la presión: P = F/A\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- P = ",f," / ",a)
        print("- P = ",p,"\n")             
    
    elif opc==5:

        print("Has seleccionado Fuerza de presión\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                p=float(input("Ingrese la presión\n "))
                a=float(input("Ingrese el área en m^2\n "))

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
        
        f=p*a
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de la fuerza de presión: F = P*A\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- F = ",p," * ",a)
        print("- F = ",f,"\n")

    elif opc==6:

        print("Has seleccionado área de presión\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                p=float(input("Ingrese la presión\n "))
                f=float(input("Ingrese el fuerza en N\n "))

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
        
        a=f/p
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área de presión: A = F/P\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- A = ",f," / ",p)
        print("- A = ",a,"\n")  

    elif opc==7:

        print("Has seleccionado presión hidrostatica\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                d=float(input("Ingrese la densidad en kg/m^3 \n "))
                g=float(input("Ingrese la gravedad en m/s^2\n "))
                h=float(input("Ingrese la altura o profundidad en m\n "))

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
        
        p=d*g*h

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Presión Hidrostatica: P = D*g*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- P = ",d," * ",g," * ",h)
        print("- P = ",p," N/m^2\n")

    elif opc==8:

        print("Has seleccionado Densidad en Presión hidrostatica\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                p=float(input("Ingrese la presión en N/m^2 \n "))
                g=float(input("Ingrese la gravedad en m/s^2\n "))
                h=float(input("Ingrese la altura o profundidad en m\n "))

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
        
        d=p/(g*h)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Densidad en Presión Hidrostatica: D = P/g*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- D = ",p," / (",g," * ",h,")")
        print("- D = ",p," / ",g*h)
        print("- D = ",d,"\n")

    elif opc==9:

        print("Has seleccionado Profundidad en Presión hidrostatica\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                p=float(input("Ingrese la presión en N/m^2 \n "))
                g=float(input("Ingrese la gravedad en m/s^2\n "))
                d=float(input("Ingrese la densidad en Kg/m^3\n"))

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
        
        h=p/(g*d)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Profundidad en Presión Hidrostatica: h = P/g*d\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- h = ",p," / (",g," * ",d,")")
        print("- h = ",p," / ",g*d)
        print("- h = ",h,"\n")            
    
    elif opc==10:

        print("Has seleccionado Calor\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa \n "))
                ce=float(input("Ingrese el calor especifico\n "))
                ti=float(input("Ingrese la temperatura inicial\n"))
                tf=float(input("Ingrese la temperatura final\n"))

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
        
        q=ce*m*(tf-ti)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Calor: Q = CE*M*(TF-TI)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- Q = ",ce," * ",m," * (",tf," - ",ti,")")
        print("- Q = ",ce," * ",m," * ",tf-ti)
        print("- Q = ",q,"\n") 

    elif opc==11:

        print("Has seleccionado Calor Especifico\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa \n "))
                q=float(input("Ingrese el calor\n "))
                ti=float(input("Ingrese la temperatura inicial\n"))
                tf=float(input("Ingrese la temperatura final\n"))

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
        
        ce=q/(m*(tf-ti))

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Calor Específico: CE = Q/M*(TF-TI)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- CE = ",q," / (",m," * (",tf," - ",ti,"))")
        print("- CE = ",q," / (",m," * ",tf-ti,")")
        print("- CE = ",q," / ",m*(tf-ti))
        print("- CE = ",ce,"\n")    

    elif opc==12:

        print("Has seleccionado Temperatura Final\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa \n "))
                q=float(input("Ingrese el calor\n "))
                ti=float(input("Ingrese la temperatura inicial\n"))
                ce=float(input("Ingrese el Calor Especifico\n"))

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
        
        tf=(ti+q)/(ce*m)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Temperatura Final: Tf = (TI+Q)/(CE*M)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- TF = (",ti," + ",q,") / (",ce," * ",m,")")
        print("- TF = ",ti+q," / ",ce*m)
        print("- TF = ",tf,"\n")   

    elif opc==13:

        print("Has seleccionado Temperatura Inicial\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                m=float(input("Ingrese la masa \n "))
                q=float(input("Ingrese el calor\n "))
                tf=float(input("Ingrese la temperatura final\n"))
                ce=float(input("Ingrese el Calor Especifico\n"))

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
        
        ti=(tf-q)/(ce*m)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de Temperatura Inicial: Ti = (TF-Q)/(CE*M)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- Ti = (",tf," - ",q,") / (",ce," * ",m,")")
        print("- Ti = ",tf-q," / ",ce*m)
        print("- Ti = ",ti,"\n")                      

    elif opc==14:
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