#Se importa la libreria os que permite utilizar 
#varias funciones propias del sistema operativo
import os
#Se importa la libreria math para usar barias funciones matemáticas
import math
"""
Punto B
Realizar el siguiente listado de fórmulas algoritmos independientes, 
donde el usuario digite el valor década termino,
"""

"""
El siguiente algoritmo el área y perimetro de diferentes figuras
geometricas a través de su formula algebraica
"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa permite calcular el área y perimetro de algunas figuras\n ")

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
                    "Ingrese 1 para Rectangulo\n"
                    "Ingrese 2 para Triángulo con altura\n"
                    "Ingrese 3 para Triángulo con semiperimetro\n"
                    "Ingrese 4 para Triangulo Rectangulo (Pitagoras)\n"
                    "Ingrese 5 para Trapecio\n"
                    "Ingrese 6 para Cuadrado\n"
                    "Ingrese 7 para Circunferencia\n"
                    "Ingrese 8 para Paralelogramo\n"
                    "Ingrese 9 para salir\n"
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
        
        print("Has seleccionado área y perímetro para un Rectangulo\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                base=float(input("Ingrese la base del rectangulo o lado mas largo\n "))
                altura=float(input("Ingrese la altura del rectangulo o lado mas corto\n "))
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
    
        perimetro=(2*base)+(2*altura)
        area=base*altura
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = 2a + 2b\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = (2*",base,")+(2*",altura,")")
        print("- p = ",2*base,"+",2*altura,")")
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = a*b\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = ",base,"*",altura)
        print("- a = ",area," unidades cuadradas\n")
        
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
    
    elif opc==2:
        
        print("Has seleccionado área y perímetro para un Triángulo con altura\n ")
        
         #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                base=float(input("Ingrese la base del triangulo\n "))
                altura=float(input("Ingrese la altura del triangulo\n "))
                l1=float(input("Ingrese el lado 1 del triangulo\n "))
                l2=float(input("Ingrese el lado 2 del triangulo\n "))
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
    
        perimetro=base+l1+l2
        area=(base*altura)/2
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = base + lado1 + lado2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = ",base," + ",l1," + ",l2)
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = (base*altura)/2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = (",base,"*",altura,")/2")
        print("- a = ",base*altura,"/2")
        print("- a = ",area," unidades cuadradas\n") 

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

    elif opc==3:

        print("Has seleccionado área y perímetro para un Triángulo con semiperimetro\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese el lado 1 del triangulo\n "))
                l2=float(input("Ingrese el lado 2 del triangulo\n "))
                l3=float(input("Ingrese el lado 3 del triangulo\n "))

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
    
        perimetro=l1+l2+l3
        semiperimetro=perimetro/2
        area=math.sqrt((semiperimetro)*(semiperimetro-l1)*(semiperimetro-l2)*(semiperimetro-l3))
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = a + b + c\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = ",l1," + ",l2," + ",l3)
        print("- p = ",perimetro," unidades\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de semiperímetro: p = (a + b + c)/2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- s = (",l1," + ",l2," + ",l3,")/2")
        print("- s = ",perimetro,"/2")
        print("- s = ",semiperimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = √s(s−a)(s−b)(s−c)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = √",semiperimetro,"*(",semiperimetro,"-",l1,")*(",semiperimetro,"-",l2,")*(",semiperimetro,"-",l3,")")
        print("- a = √",semiperimetro,"*(",semiperimetro-l1,")*(",semiperimetro-l2,")*(",semiperimetro-l3,")")
        print("- a = √",semiperimetro*(semiperimetro-l1)*(semiperimetro-l2)*(semiperimetro-l3))
        print("- a = ",area," unidades cuadradas\n") 

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

    elif opc==4:

        print("Has seleccionado área y perímetro para un Triangulo Rectangulo (Pitagoras)\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese el cateto 1 del triangulo\n "))
                l2=float(input("Ingrese el cateto 2 del triangulo\n "))

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
        
        h=math.sqrt((l1**2)+(l2**2))
        perimetro=l1+l2+h
        area=(l1*l2)/2
    
        #Muestra paso a paso la resolución de la formula
        print("Teorema de pitágoras: h = √a^2 + b^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- h = √(",l1,"^2) + (",l2,"^2)")
        print("- h = √(",l1**2,") + (",l2**2,")")
        print("- h = √",(l1**2) + (l2**2))
        print("- h = ",h," unidades\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = a + b + h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = ",l1," + ",l2," + ",h)
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = a*b/2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = (",l1,"*",l2,")/2")
        print("- a = ",l1*l2,"/2")
        print("- a = ",area," unidades cuadradas\n") 

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
    
    elif opc==5:

        print("Has seleccionado área para un Trapecio\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese la base menor del Trapecio\n "))
                l2=float(input("Ingrese la base mayor del Trapecio\n "))
                h=float(input("Ingrese la altura del Trapecio\n "))

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
        
        area=((l1+l2)/2)*h
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = (a+b/2)*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = ((",l1,"+",l2,")/2)*",h)
        print("- a = (",l1+l2,"/2)*",h)
        print("- a = ",(l1+l2)/2,"*",h)
        print("- a = ",area," unidades cuadradas\n") 

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

    elif opc==6:

        print("Has seleccionado área para un Cuadrado\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese un lado del Cuadrado\n "))

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
        
        perimetro=l1*4
        area=l1**2

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = 4*a\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = 4*",l1)
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: área = a^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = ",l1,"^2")
        print("- a = ",area," unidades cuadradas\n") 

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

    elif opc==7:

        print("Has seleccionado área para una Circunferencia\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                r=float(input("Ingrese el radio de la circunferencia\n "))

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
        
        perimetro=2*(math.pi)*r
        area=math.pi*(r**2)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = 2pi*r\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = 2*",math.pi,"*",r)
        print("- p = ",2*math.pi,"*",r)
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = pi*r^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = ",math.pi,"*",r,"^2")
        print("- a = ",math.pi,"*",r**2)
        print("- a = ",area," unidades cuadradas\n") 

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
    
    elif opc==8:

        print("Has seleccionado área para un Paralelogramo\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                base=float(input("Ingrese la base del paralelogramo\n "))
                altura=float(input("Ingrese la altura del paralelogramo\n "))

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
        
        perimetro= (2*base) + (2*altura)
        area=base*altura

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de perímetro: p = 2*Base + 2*Altura\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- p = 2*",base," + 2*",altura)
        print("- p = ",2*base," + ",2*altura)
        print("- p = ",perimetro," unidades\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área: a = Base*Altura\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- a = ",base,"*",altura)
        print("- a = ",area," unidades cuadradas\n") 

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

    elif opc==9:
        #Limpiamos la consola
        os.system('cls')
        print("Has salido del programa")
        exit()       