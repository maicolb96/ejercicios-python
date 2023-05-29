#Importa la libreria os que permite usar el metodo system para usar codigo MSDOS
import os
"""
Punto A
Realizar el siguiente listado de fórmulas algoritmos independientes, 
donde el usuario digite el valor década termino.
"""
"""
El siguiente algoritmo calcula el producto de una potencia,
la potencia de potra potencia, potencia con exponente nulo, 
potencia con exponente negativo y division de potencias

"""
#Limpiamos la consola
os.system('cls')

#Se imprime una explicacion de lo que hace el programa
print("Este programa muestra algunas operaciones con potencias\n ")

#Se lee un valor por consola y se asigna a una variable entera
opc=int(input(
        "Ingrese 1 para producto de potencias\n"
        "Ingrese 2 para potencia de una potencia\n"
        "Ingrese 3 para potencia con exponente nulo\n"
        "Ingrese 4 para potencia con exponente negativo\n"
        "Ingrese 5 para división de potencias\n"
        ))

#Limpiamos la consola
os.system('cls')


#Este if verifica la opcion que el usuario ingresó y se guardo en la variable opc
if opc==1:
    
    print("Has seleccionado un producto de potencias\n ")
    
    #Se capturan los datos de a potencia
    base_a=int(input("Ingrese la base de la primera potencia\n"))
    exp_a=int(input("Ingrese el exponente de la primera potencia\n"))

    base_b=int(input("Ingrese la base de la segunda potencia\n"))
    exp_b=int(input("Ingrese el exponente de la segunda potencia\n"))
    
    #Limpiamos la consola
    os.system('cls')
    
    #Se verifica si las bases de ambas potencias son iguales
    if base_a == base_b:
       
        #Se realiza la ecuación y se guarda en la variable res
        res = base_a**(exp_a+exp_b)

        #Muestra paso a paso la resolución de la formula
        print("Operación algebraica ",base_a,"^",exp_a," * ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) * (a^n) = a^(m+n)\n")
        print("- ",base_a,"^",exp_a," * ",base_b,"^",exp_b," = ",base_a,"^(",exp_a,"+",exp_b,")")
        print("- ",base_a,"^(",exp_a,"+",exp_b,")"," = ",base_a,"^",(exp_a+exp_b))
        print("- ",base_a,"^",(exp_a+exp_b)," = ",res,"\n")

    #Se verifica si las bases de ambas potencias son diferentes y los exponentes iguales
    elif base_a != base_b and exp_a == exp_b:
        
        #Se realiza la ecuación y se guarda en la variable res
        res = (base_a*base_b)**exp_a

        #Muestra paso a paso la resolución de la formula
        print("Operación algebraica ",base_a,"^",exp_a," * ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) * (b^m) = (a*b)^m\n")
        print("- ",base_a,"^",exp_a," * ",base_b,"^",exp_b," = (",base_a,"*",base_b,")^",exp_a)
        print("- (",base_a,"*",base_b,")^",exp_a," = ",(base_a*base_b),"^",exp_a)
        print("- ",(base_a*base_b),"^",exp_a," = ",res,"\n")
    
    #Se verifica si las bases de ambas potencias son diferentes y los exponentes diferentes
    elif base_a != base_b and exp_a != exp_b:

        #Se realiza la ecuación y se guarda en la variable res
        res = (base_a**exp_a) * (base_b**exp_b) 

        #Muestra paso a paso la resolución de la formula    
        print("Operación algebraica ",base_a,"^",exp_a," * ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) * (b^n) = (a^m) * (b^n)\n")
        print("- ",base_a,"^",exp_a," = ",base_a**exp_a)
        print("- ",base_b,"^",exp_b," = ",base_b**exp_b)
        print("- ",base_a**exp_a," * ",base_b**exp_b," = ",res,"\n")

elif opc==2:

    print("Has seleccionado potencia de una potencia\n ")
    
    #Se capturan los datos de a potencia
    base_a=int(input("Ingrese la base de la primera potencia\n"))
    exp_a=int(input("Ingrese el exponente de la primera potencia\n"))

    exp_b=int(input("Ingrese el segundo exponente\n"))
    
    #Limpiamos la consola
    os.system('cls')
    
    #Se realiza la ecuación y se guarda en la variable res
    res = base_a**(exp_a*exp_b)   

    #Muestra paso a paso la resolución de la formula  
    print("Operación algebraica (",base_a,"^",exp_a,")^",exp_b," = ",res,"\n ")
    print("PASOS\n ")
    print("Aplicar ley (a^m)^n = a^(m*n)\n")
    print("- (",base_a,"^",exp_a,")^",exp_b," = ",base_a,"^(",exp_a,"*",exp_b,")")
    print("- ",base_a,"^(",exp_a,"*",exp_b,") = ",base_a,"^",(exp_a*exp_b))
    print("- ",base_a,"^",(exp_a*exp_b)," = ",res,"\n")

elif opc==3:

    print("Has seleccionado potencia con exponente nulo\n ")
    
    #Se capturan los datos de a potencia
    base_a=int(input("Ingrese la base de la potencia\n"))
    exp_a=0

    #Limpiamos la consola
    os.system('cls')
    
    #Se verifica que la base sea mayor a 0
    if base_a>0:

        #Se realiza la ecuación y se guarda en la variable res
        res = base_a**(exp_a)  

        #Muestra paso a paso la resolución de la formula   
        print("Operación algebraica ",base_a,"^0 = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley a^0 = 1\n")
        print("- ",base_a,"^0 = ",res,"\n ")
    else:
        #Si la base es igual a 0 se indica que debe ser mayor a cero
        print("0^0 no está definido, ingrese una base mayor que 0")       

elif opc==4:

    print("Has seleccionado potencia con exponente negativo\n ")
    
    #Se capturan los datos de a potencia
    base_a=int(input("Ingrese la base de la potencia\n"))
    exp_a=int(input("Ingrese el exponente de la potencia\n"))

    #Limpiamos la consola
    os.system('cls')
    
    #Se verifica que el exponente sea menor a 0
    if exp_a<0:

        #Se realiza la ecuación y se guarda en la variable res
        res = (1/base_a)**exp_a    

        #Muestra paso a paso la resolución de la formula
        print("\nOperación algebraica ",base_a,"^",exp_a," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley a^-n = (1/a)^n\n")
        print("- ",base_a,"^",exp_a," = (1/",base_a,")^",abs(exp_a))
        print("- (1/",base_a,")^",abs(exp_a)," = ",(1/base_a),"^",abs(exp_a))
        print("- ",(1/base_a),"^",abs(exp_a)," = ",res,"\n")
    else:
        #Si el exponente es mayor a 0 se indica que debe ser negativo
        print("Ingrese un exponente negativo")          

elif opc==5:
    
    print("Has seleccionado una división de potencias\n ")

    #Se capturan los datos de a potencia
    base_a=int(input("Ingrese la base de la primera potencia\n"))
    exp_a=int(input("Ingrese el exponente de la primera potencia\n"))

    base_b=int(input("Ingrese la base de la segunda potencia\n"))
    exp_b=int(input("Ingrese el exponente de la segunda potencia\n"))
    
    #Limpiamos la consola
    os.system('cls')
    
    #Se verifica si las bases de ambas potencias son iguales
    if base_a == base_b:

        #Se realiza la ecuación y se guarda en la variable res       
        res = base_a**(exp_a-exp_b)

        #Muestra paso a paso la resolución de la formula        
        print("Operación algebraica ",base_a,"^",exp_a," / ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) / (a^n) = a^(m-n)\n")
        print("- ",base_a,"^",exp_a," / ",base_b,"^",exp_b," = ",base_a,"^(",exp_a,"-",exp_b,")")
        print("- ",base_a,"^(",exp_a,"-",exp_b,")"," = ",base_a,"^",(exp_a-exp_b))

        #Si la resta de exponentes es menor a 0 se aplica la ley de exponente negativo
        if exp_a-exp_b<0:
            print("\nAplicar ley a^-n = (1/a)^n\n")
            print("- ",base_a,"^",exp_a-exp_b," = (1/",base_a,")^",abs(exp_a-exp_b))
            print("- (1/",base_a,")^",abs(exp_a-exp_b)," = ",(1/base_a),"^",abs(exp_a-exp_b))
            print("- ",(1/base_a),"^",abs(exp_a-exp_b)," = ",res,"\n")  
        else: 
            #Si la resta de exponentes es mayor o igual a 0 se imprime el paso siguiente
            print("- ",base_a,"^",(exp_a-exp_b)," = ",res,"\n")

    #Se verifica si las bases de ambas potencias son diferentes y los exponentes iguales
    elif base_a != base_b and exp_a == exp_b:

        #Se realiza la ecuación y se guarda en la variable res
        res = (base_a/base_b)**exp_a

        #Muestra paso a paso la resolución de la formula
        print("Operación algebraica ",base_a,"^",exp_a," / ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) / (b^m) = (a/b)^m\n")
        print("- ",base_a,"^",exp_a," / ",base_b,"^",exp_b," = (",base_a,"/",base_b,")^",exp_a)
        print("- (",base_a,"/",base_b,")^",exp_a," = ",(base_a/base_b),"^",exp_a)
        print("- ",(base_a/base_b),"^",exp_a," = ",res,"\n")

    #Se verifica si las bases de ambas potencias son diferentes y los exponentes diferentes
    elif base_a != base_b and exp_a != exp_b:

        #Se realiza la ecuación y se guarda en la variable res
        res = (base_a**exp_a) / (base_b**exp_b)     

        #Muestra paso a paso la resolución de la formula            
        print("Operación algebraica ",base_a,"^",exp_a," / ",base_b,"^",exp_b," = ",res,"\n ")
        print("PASOS\n ")
        print("Aplicar ley (a^m) / (b^n) = (a^m) / (b^n)\n")
        print("- ",base_a,"^",exp_a," = ",base_a**exp_a)
        print("- ",base_b,"^",exp_b," = ",base_b**exp_b)
        print("- ",base_a**exp_a," / ",base_b**exp_b," = ",res,"\n")
