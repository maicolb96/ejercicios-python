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
                    "Ingrese 1 para Prisma Rectangular\n"
                    "Ingrese 2 para Piramide Pentagonal Regular\n"
                    "Ingrese 3 para Paralelepipedo Recto\n"
                    "Ingrese 4 para Cilindro\n"
                    "Ingrese 5 para Cubo\n"
                    "Ingrese 6 para Cono\n"
                    "Ingrese 7 para Esfera\n"
                    "Ingrese 8 para Salir\n"
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
        
        print("Has seleccionado área y volúmen para un Prisma Rectangular\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese el primer lado de la base del Prisma\n"))
                l2=float(input("Ingrese el segundo lado de la base del Prisma\n"))
                l3=float(input("Ingrese el tercer lado de la base del Prisma\n"))
                l4=float(input("Ingrese el cuarto lado de la base del Prisma\n"))
                altura=float(input("Ingrese la altura del rectangulo del Prisma\n"))
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
    
        perimetro_base=l1+l2+l3+l4
        area_lateral=perimetro_base*altura
        area_base=l1*l2
        area_total=area_lateral+(2*area_base)
        volumen=area_base*altura
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área lateral: areaL = (a*h) + (b*h) + (c*h) + (d*h)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaL = (",l1,"*",altura,") + (",l2,"*",altura,") + (",l3,"*",altura,") + (",l4,"*",altura,")")
        print("- areaL = ",l1*altura," + ",l2*altura," + ",l3*altura," + ",l4*altura)
        print("- areaL = ",area_lateral," unidades cuadradas\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área de la Base: areaB = a*b\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaB = ",l1,"*",l2)
        print("- areaB = ",area_base," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = areaL + (2*areaB)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = ",area_lateral," + (2*",area_base,")")
        print("- areaT = ",area_lateral," + ",(2*area_base))
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = areaB*h)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = ",area_base," * ",altura)
        print("- v = ",volumen," unidades cubicas\n")       
    
    elif opc==2:
        
        """
        NOTA: para efectos del ejercicio se asume que se trata de una piramide
        pentagonal según la figura del taller, al no espesificarse si es una pirámide
        regular, vamos a asumir que es así y que todos los lados de la base miden lo mismo. 
        """
        print("Has seleccionado área y volúmen para una pirámide pentagonal regular\n ")
        
         #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese la medida de los lados de la base\n "))
                ap=float(input("Ingrese el apotema de la base\n "))
                h=float(input("Ingrese la altura normal de la pirámide\n "))
                hl=float(input("Ingrese la altura de inclinación de las caras laterales\n "))
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
        
        perimetro_base=5*l1
        area_lateral=0.5*(perimetro_base*hl)
        area_base=(l1*5*ap)/2
        area_total=area_base+area_lateral
        volumen=(1/3)*(area_base)*h
    
         #Muestra paso a paso la resolución de la formula
        print("Ecuación de área lateral: areaL = 1/2(pB*hl)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaL = 1/2*(",perimetro_base,"*",hl,")")
        print("- areaL = 0.5*",perimetro_base*hl)
        print("- areaL = ",area_lateral," unidades cuadradas\n")
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área de la Base: areaB = (5*a*ap)/2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaB = (5 *",l1," * ",ap,")/2")
        print("- areaB = ",5 *l1*ap,"/2")
        print("- areaB = ",area_base," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = areaL + areaB\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = ",area_lateral," + ",area_base)
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = 1/3(areaB*h)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = 1/3(",area_base," * ",h,")")
        print("- v = 0.33 * ",area_base*h)
        print("- v = ",volumen," unidades cubicas\n")

    elif opc==3:

        print("Has seleccionado área y volúmen de un paralelepípedo recto\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese el lado 1 del paralelepípedo recto\n "))
                l2=float(input("Ingrese el lado 2 del paralelepípedo recto\n "))
                h=float(input("Ingrese la altura del paralelepípedo recto\n "))

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
    
        area_lateral=((2*l1)+(2*l2))*h
        area_total=area_lateral+2*(l1*l2)
        volumen=l1*l2*h
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área lateral: areaL = (2a + 2b)*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaL = (2 * ",l1," + 2 * ",l2,") * ",h)
        print("- areaL = (",2 * l1," + ",2 * l2,") * ",h)
        print("- areaL = ",(2 * l1)+(2 * l2)," * ",h)
        print("- areaL = ",area_lateral," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = areaL + 2(a*b)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = ",area_lateral," + 2 * (",l1," * ",l2,")")
        print("- areaT = ",area_lateral," + ",2 * (l1 * l2))
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = a * b * h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = ",l1," * ",l2," * ",h)
        print("- v = ",volumen," unidades cubicas\n") 

    elif opc==4:

        print("Has seleccionado área y volúmen para un Cilindro\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                h=float(input("Ingrese la altura del cilindro\n "))
                r=float(input("Ingrese el radio del cilindro\n "))

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
        
        area_lateral=2*(math.pi)*r*h
        area_total=2*math.pi*r*(r+h)
        volumen=math.pi*(r**2)*h
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área lateral: areaL = 2piR*h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaL = 2 * ",math.pi," * ",r," * ",h)
        print("- areaL = ",area_lateral," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = 2piR(r+h)\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = 2 * ",math.pi," * ",r," * (",r," + ",h,")")
        print("- areaT = 2 * ",math.pi," * ",r," * ",r+h)
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = (piR^2)h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = ",math.pi," * (",r,"^2) *",h)
        print("- v = ",math.pi," * ",r**2," * ",h)
        print("- v = ",volumen," unidades cubicas\n")              
    
    elif opc==5:

        print("Has seleccionado área para un Cubo\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                l1=float(input("Ingrese el lado del cubo\n "))

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
        
        area_total=6*(l1**2)
        volumen=l1**3
    
        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = 6a^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = 6 * (",l1,"^ 2)")
        print("- areaT = 6 * ",l1**2)
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = a^3\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = ",l1,"^ 3")
        print("- v = ",volumen," unidades cubicas\n") 

    elif opc==6:

        print("Has seleccionado área y volúmen para un Cono\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                r=float(input("Ingrese el radio de la base del cono\n "))
                h=float(input("Ingrese la altura del cono\n "))
                ap=float(input("Ingrese el apotema del cono\n "))

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
        
        area_lateral=math.pi*r*ap
        area_total=area_lateral + (math.pi*(r**2))
        volumen=(1/3)*(math.pi*(r**2))*h

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área lateral: areaL = piRS\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaL = ",math.pi," * ",r," * ",ap)
        print("- areaL = ",area_lateral," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = areaL + piR^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = ",area_lateral," + (",math.pi," * (",r,"^2))")
        print("- areaT = ",area_lateral," + (",math.pi," * ",r**2,")")
        print("- areaT = ",area_lateral," + ",math.pi * (r**2))
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = 1/3(piR^2)h\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = 1/3 * (",math.pi," * (",r,"^2)) *",h)
        print("- v = 0.33 * (",math.pi," * ",r**2,") *",h)
        print("- v = 0.33 * ",math.pi * (r**2)," * ",h)
        print("- v = ",volumen," unidades cubicas\n")  

    elif opc==7:

        print("Has seleccionado área para una esfera\n ")
        
        #Se define una variable verdadera para entrar en un ciclo 
        state=True
    
        #Se comienza un bucle que termina solo cuando state es Falso, solo ocurre
        #cuando se ingresa una opción valida numérica
        while state==True:

            #Se controlan los errores con la sentencia Try que ejecuta el código si no hay un error  
            try:
                r=float(input("Ingrese el radio de la esfera\n "))

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
        
        area_total=4*math.pi*(r**2)
        volumen=(4/3)*math.pi*(r**3)

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de área total: areaT = 4piR^2\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- areaT = 4 * (",math.pi," * (",r,"^ 2))")
        print("- areaT = 4 * (",math.pi," * ",r**2,")")
        print("- areaT = 4 * ",math.pi," * ",r**2)
        print("- areaT = ",area_total," unidades cuadradas\n")

        #Muestra paso a paso la resolución de la formula
        print("Ecuación de volúmen: v = 4/3piR^3\n ")
        print("PASOS\n ")
        print("Aplicar la fórmula:\n")
        print("- v = 4/3 * (",math.pi," * (",r,"^ 3))")
        print("- v = 4/3 * (",math.pi," * ",r**3,")")
        print("- v = 4/3 * ",math.pi," * ",r**3)
        print("- v = ",volumen," unidades cubicas\n")  
    
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