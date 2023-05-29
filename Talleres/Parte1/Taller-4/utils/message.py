#Se importa la libreria colored que permite usar colores para las cadenas de texto
from utils import my_color

class Message:

    def format_message(self,code,arg1,arg2,arg3):
        
        #Instancia o creación de objeto color, se utiliza el init para dar forma (atributos)
        cl1 = my_color.Color(["red","blue","green"])

        #No se usa el match por que estoy trabajando con la versión 3.9 de python.
        
#-------MENSAJES PARA ERRORES----------  
      
        if code == 'Ex001':
            msj=f"{cl1.c[0]}Error, el día no puede ser menor a 1 ni mayor a 31."
        elif code == 'Ex002':
            msj=f"{cl1.c[0]}Error, el mes no puede ser mayor a 12 o menor a 1."
        elif code == 'Ex003':
            msj=f"{cl1.c[0]}Error, el año debe tener 4 díjitos."
        elif code == 'Ex004':
            msj=f"{cl1.c[0]}Vuelva a ingresar los datos por favor."
        elif code == 'Ex005':
            msj=f"{cl1.c[0]}No se aceptan letras o caracteres. Vuelva a ingresar los datos porfavor."            
        elif code == 'Ex006':
            msj=f"{cl1.c[0]}El valor no puede ser menor que cero.\n"
        elif code == 'Ex007':
            msj=f"{cl1.c[0]}El valor debe ser mínimo de 2 * para poder formar el cuadrado." 
        elif code == 'Ex008':
            msj=f"{cl1.c[0]}No se permite el ingreso a menores de 5 años." 
        elif code == 'Ex009':
            msj=f"{cl1.c[0]}No vas a pagar nada, por favor retirare o compra algo." 
        elif code == 'Ex010':
            msj=f"{cl1.c[0]}Ingresa un valor mayor a cero.\n"                 

#-------MENSAJES INFORMATIVOS----------

        if code == 'INFx001':
            msj=f'{cl1.c[1]}Este algoritmo recibe una fecha en formato {cl1.c[2]}DD/MM/AAAA \n{cl1.c[1]}de forma númerica y devuelve la fecha con el mes en texto.\n'    
        elif code == 'INFx002':
            msj=f"La fecha es: {arg1} de {arg2} del {arg3}.\n"
        elif code == 'INFx003':
            msj=f"{cl1.c[1]}Este algoritmo recoge un valor entero e imprime un cuadrado de lado igual al entero recibido.\n"        
        elif code == 'INFx004':
            msj=f"{cl1.c[1]}Este algoritmo recibe una altura y devuelve una escalera invertida de asteriscos con esa altura.\n" 
        elif code == 'INFx005':
            msj=f"{cl1.c[1]}Este algoritmo recibe un año y verifica si es Bisiesto o no.\n" 
        elif code == 'INFx006':
            msj=f"{cl1.c[1]}El año {arg1} es Bisiesto.\n"
        elif code == 'INFx007':
            msj=f"{cl1.c[1]}El año {arg1} no es Bisiesto.\n"
        elif code == 'INFx008':
            msj=f"{cl1.c[1]}Este algoritmo determinar la cantidad de dinero que el teatro deja de percibir por cada una de las categorías..\n"  
        elif code == 'INFx009':
            msj=f"{cl1.c[1]}A continuación se muestra el dinero que se deja de ganar por cada categoría a raiz de los descuentos: \n"
        elif code == 'INFx010':
            msj=f"{cl1.c[1]}Categoría {arg1}: ${arg2:.2f}"
        elif code == 'INFx011':
            msj=f"{cl1.c[1]}Sacando una bola de la bolsa..."    
        elif code == 'INFx012':
            msj=f"{cl1.c[1]}Has seleccionado la bola {arg1} ¡En hora buena tienes un descuento del {arg2}"                            
        elif code == 'INFx013':
            msj=f"{cl1.c[1]}Has seleccionado la bola {arg1}, lo sentimos no tienes ningun descuento." 
        elif code == 'INFx014':
            msj=f"{cl1.c[1]}Total: ${arg1}\nDescuento: ${arg2:.2f}\nTotal a pagar: ${(arg1-arg2):.2f}"  
        elif code == 'INFx015':
            msj=f"{cl1.c[1]}Este algoritmo determinar la cantidad de dinero que una tienda deja de ganar a raiz de los descuentos por cada compra.\n"
        elif code == 'INFx016':
            msj=f"{cl1.c[1]}Este algoritmo determinar el sueldo a pagar a cierta cantidad de obreros y las horas extra.\n" 
        elif code == 'INFx017':
            msj=f"{cl1.c[1]}Datos del trabajador número {arg1+1}.\n"
        elif code == 'INFx018':
            msj=f"{cl1.c[1]}A continuación se muestra el dinero que se debe pagar a los trabajadores: \n"   
        elif code == 'INFx019':
            msj=f"{cl1.c[1]}Este algoritmo muestra el candidato ganador de las elecciones y la cantidad de votos.\n"  
        elif code == 'INFx020':
            msj=f"{cl1.c[1]}El ganador es el candidato #{arg2} con {arg1} votos.\n"
        elif code == 'INFx021':
            msj=f"{cl1.c[1]}Artículos A: {cl1.c[2]}{arg1} unidades, {cl1.c[1]}importe total: {cl1.c[2]}${arg2:.2f}" 
        elif code == 'INFx022':
            msj=f"{cl1.c[1]}Artículos B: {cl1.c[2]}{arg1} unidades, {cl1.c[1]}importe total: {cl1.c[2]}${arg2:.2f}"
        elif code == 'INFx023':
            msj=f"{cl1.c[1]}Este algoritmo recoge la temperatura por n días y calcula la media de temperaturas y si la temperatura es 9 lo toma como error.\n" 
        elif code == 'INFx024':
            msj=f"{cl1.c[1]}Ingrese 0 en ambas temperaturas para terminar la lectura.\n"
        elif code == 'INFx025':    
            msj=f"{cl1.c[1]}Temperaturas máximas ingresadas: {cl1.c[2]}{arg1}"
        elif code == 'INFx026':    
            msj=f"{cl1.c[1]}Temperaturas mínimas ingresadas: {cl1.c[2]}{arg1}\n"
        elif code == 'INFx027':
            msj=f"{cl1.c[1]}Número de días totales: {cl1.c[2]}{(arg1+arg2)}"
        elif code == 'INFx028':
            msj=f"{cl1.c[1]}Número de días con errores: {cl1.c[2]}{arg1}"
        elif code == 'INFx029':
            msj=f"{cl1.c[1]}Número de días sin errores: {cl1.c[2]}{arg1}"
        elif code == 'INFx030':
            msj=f"{cl1.c[1]}Media de temperaturas máximas: {cl1.c[2]}{arg1:.2f}"
        elif code == 'INFx031':
            msj=f"{cl1.c[1]}Media de temperaturas mínimas: {cl1.c[2]}{arg1:.2f}"
        elif code == 'INFx032':
            msj=f"{cl1.c[1]}Número de errores (temperatura 9): {cl1.c[2]}{arg1}, {arg2:.2f}% del total\n" 
        elif code == 'INFx033':
            msj=f"{cl1.c[1]}No se han registrado temperaturas."
        elif code == 'INFx034':
            msj=f"{cl1.c[1]}Este algoritmo calcula el nuevo salario incrementando un 25% sobre el salario anterior.\n"           
        elif code == 'INFx035':
            msj=f"\n{cl1.c[1]}El nuevo salario es: {cl1.c[2]}${arg1+(arg1*0.25)}\n"
        elif code == 'INFx036':
            msj=f"\n{cl1.c[1]}Este algoritmo calcula el presupuesto de tres áreas \nde un hospital a partir de un monto dado.\n"    
        elif code == 'INFx037':
            msj=f"\n{cl1.c[1]}El presupuesto total es de: ${cl1.c[2]}{arg1}"
        elif code == 'INFx038':
            msj=f"{cl1.c[1]}El presupuesto de Ginecología es de: ${cl1.c[2]}{arg1*0.40}"
        elif code == 'INFx039':
            msj=f"{cl1.c[1]}El presupuesto de Traumatología es de: ${cl1.c[2]}{arg1*0.30}"
        elif code == 'INFx040':
            msj=f"{cl1.c[1]}El presupuesto de Pediatría es de: ${cl1.c[2]}{arg1*0.30}"    
        elif code == 'INFx041':
            msj=f"{cl1.c[1]}Este algoritmo calcula el precio de venta de un producto para ganar el 30% de utilidad.\n"       
        elif code == 'INFx042':
            msj=f"{cl1.c[1]}El precio al que debes vender el producto\npara ganar un 30% es de: ${cl1.c[2]}{arg1+(arg1*0.30)}\n"  
        elif code == 'INFx043':
            msj=f"{cl1.c[1]}Este algoritmo calcula el tiempo en minutos promedio de recorrido en una semana de un atleta.\n"
        elif code == 'INFx044':
            msj=f"{cl1.c[1]}Tiempo del día {arg1}: {cl1.c[2]}{arg2}s"
        elif code == 'INFx045':
            msj=f"{cl1.c[1]}\nEl tiempo promedio que tarda en recorrer la ruta en una semana cualquiera es: {cl1.c[2]}{arg1}s\n"  
        elif code == 'INFx046':
            msj=f"{cl1.c[1]}Este algoritmo calcula el porcentaje invertido por un frupo de 3 inversores para un proyecto.\n"          
        elif code == 'INFx047':
            msj=f"{cl1.c[1]}\nA continuación se muestran los montos invertidos y sus porcentajes: \n"
        elif code == 'INFx048':
            msj=f"{cl1.c[1]}Monto total invertido: {cl1.c[2]}{arg1}\n"    
        elif code == 'INFx049':
            msj=f"{cl1.c[1]}{arg1}: ${cl1.c[2]}{arg2} equivalente al {arg3}%"
            

#-------MENSAJES PARA INPUTS----------   
     
        if code == 'INPx001':
            msj=f"{cl1.c[2]}Ingrese el "+arg1+": "
        elif code == 'INPx002':
            msj=f"{cl1.c[2]}Ingrese la cantidad de * que formarán la figura: " 
        elif code == 'INPx003':
            msj=f"{cl1.c[2]}Ingrese el año en formato de 4 números: "
        elif code == 'INPx004':
            msj=f"{cl1.c[2]}Ingrese la cantidad de asientos que se venderán: "    
        elif code == 'INPx005':
            msj=f"{cl1.c[2]}Ingrese la edad del cliente {arg1}: " 
        elif code == 'INPx006':
            msj=f"{cl1.c[2]}Ingrese el valor del asiento {arg1}: "
        elif code == 'INPx007':
            msj=f"{cl1.c[2]}Ingrese el total que debe pagar: "
        elif code == 'INPx008':
            msj=f"{cl1.c[2]}Ingrese la cantidad de obreros a liquidar: "
        elif code == 'INPx009':
            msj=f"{cl1.c[2]}Ingrese el nombre del trabajador {arg1}: "                           
        elif code == 'INPx010':
            msj=f"{cl1.c[2]}Ingrese la cantidad de horas trabajadas para {arg1}: " 
        elif code == 'INPx011':
            msj=f"{cl1.c[2]}Ingrese el valor de la hora laboral para {arg1}: "  
        elif code == 'INPx012':
            msj=f"{cl1.c[2]}La cantidad de votos para el candidato #{arg1}: "
        elif code == 'INPx013':
            msj=f"{cl1.c[2]}Temperatura máxima del día {arg1}: "
        elif code == 'INPx014':
            msj=f"{cl1.c[2]}Temperatura mínima del día {arg1}: "
        elif code == 'INPx015':
            msj=f"{cl1.c[2]}Ingrese el salario anterior: " 
        elif code == 'INPx016':
            msj=f"{cl1.c[2]}Ingrese el presupuesto total para el hospital: \n"
        elif code == 'INPx017':
            msj=f"{cl1.c[2]}Ingrese el costo del producto comprado: \n"
        elif code == 'INPx018':
            msj=f"{cl1.c[2]}Ingrese el tiempo en minutos del día {arg1}: \n"
        elif code == 'INPx019':
            msj=f"{cl1.c[2]}Ingrese el monto invertido del {arg1}: \n"        
            
        return msj
