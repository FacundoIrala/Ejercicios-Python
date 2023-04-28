# FUNCIONES
# Dividir el programa, para comprender que estamos haciendo
# Depuracion, a ese modulo
# Modificacion al modulo
# Son repetitivas, osea reutilizables
# Independencia del codigo, son independientes entre si

#VARIABLES INCORRECTAS

# def sumar_numeros()->None:#Implentacion de la funciones
#     primer_numero = int(input("Ingrese el primero numero: "))
#     segundo_numero = int(input("Ingrese el primero numero: "))#vienen de afuera

#     suma = primer_numero + segundo_numero

#     print("La suma es: ", suma)# muestro resultado

# def restar_numeros()->int: #Implentacion de la funcion
#     primer_numero = int(input("Ingrese el primero numero: "))
#     segundo_numero = int(input("Ingrese el primero numero: "))

#     resta = primer_numero - segundo_numero

#     return resta# devuelvo el resultado,generando independencia de codigo y funcion

# def multiplicar_numeros(primer_numero:int, segundo_numero:int)->None:#variables locales
#     multiplicacion = primer_numero * segundo_numero
#     print("El resultado de la multiplicacion es: {multiplicacion}")


def dividir_numeros (primer_numero:int, segundo_numero:int)->float:
    division = None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero
    return division

def sumar_numeros(primer_numero:int, segundo_numero:int)->int:
    suma = primer_numero + segundo_numero
    return suma

def restar_numeros(primer_numero:int, segundo_numero:int)->int:
    restar = primer_numero + segundo_numero
    return restar

def multiplicar_numeros(primer_numero:int, segundo_numero:int)->int:
    multiplicar = primer_numero + segundo_numero
    return multiplicar

#               RETORNO   PARAMETROS    FUNCIONA?
#SUMA              NO         NO            NO
#RESTAR            SI         NO            INTERMEDIO    
#MULTIPLICAR       NO         SI            INTERMEDIO
#DIVIDIR           SI         SI            OPTIMA

bandera_ingreso = False

while True:
    opcion = int (input("Ingrese numero\n1. Restar \n2. Restar\n3. Multiplicar\n4. Suma\n5. Salir\nIngrese una opcion"))
    match opcion:
        case 1: 
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese un numero: "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                resultado = restar_numeros(x,y)
                print(f"El resultado de la  resta es: {resultado}")
            else:
                print("No se ingresaron los numeros")
        case 3:
            resultado = multiplicar_numeros(x,y)
            print(f"El resultado de la multiplicacion es: {resultado}")
        case 4:
            resultado = dividir_numeros(x,y)
            if resultado != None:                
                print(f"El resultado de la division es: {resultado}")
            else:
                print("Error, no se puede dividir por 0")
        case 5:
            resultado = sumar_numeros(x,y)
            print(f"El resultado de la sumar es: {resultado}")
        case 6: 
                break


print("Hola bienvenido a mi programa")

sumar_numeros()#LLmada de la funcion

print("Muchas gracias!")

resultad_resta = restar_numeros()
print(f"el resultado de la resta es: {resultad_resta}")

multiplicar_numeros(5,9)#paramatros actuales, hardcodeado

x = int(input("Ingrese un numero: "))
y = int(input("Ingerese un numero"))
multiplicar_numeros(x,y)

resultado_division = dividir_numeros(6,2)#forma optima
print(f"el resultado de la resta es: {resultado_division}")

resultado_division = dividir_numeros(x,y)
if resultado_division != None:
    print(f"el resultado de la resta es: {resultado_division}")
else:
    print("El divisor es 0")




